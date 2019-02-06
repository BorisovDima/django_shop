

function getURLParameter(sUrl, sParam) {
        let sPageURL = sUrl.substring(sUrl.indexOf('?') + 1);
        let sURLVariables = sPageURL.split('&');
        for (let i = 0; i < sURLVariables.length; i++) {
            let sParameterName = sURLVariables[i].split('=');
            if (sParameterName[0] == sParam) {
                return sParameterName[1];
            }
        }
}



$(document).ready(function(){


        function init() {
              console.log(document.body.querySelectorAll('.pagination > li > a'))
              document.body.querySelectorAll('.pagination > li > a').
              forEach( function(event){
                   var href = event.href
                   if (!href.endsWith('#')) {
                       var param = getURLParameter(href, 'page')
                       event.setAttribute('data-action', 'paginate')
                        event.setAttribute('data-param', param)
                        event.removeAttribute('href')
                        $(event).on('click', function() { load_product(param) })
                    }

              })
        }

       function load_product(page) {
                var querystring = getFormData($('#filter-form'))
                console.log(querystring)
                querystring['page'] = page
                $.ajax({
                        url: '/products/',
                        method: 'GET',
                        data: querystring,
                        success: function(json) {
                                $('#list-products').html(json['html'])
                                init()
                                var path = window.location.pathname + '?page=' + page
                                window.history.pushState({route: path}, "", path)
                        },
                        error: function(data) {
                            console.log('Invalid')
                        },
                 })
             }


load_product(getURLParameter(window.location.href, 'page') || '1' )

$('#filter-form-submit').on('click', function() {
    load_product('1')

})

function getFormData($form){
    var unindexed_array = $form.serializeArray();
    var indexed_array = {};

    $.map(unindexed_array, function(n, i){
        indexed_array[n['name']] = n['value'];
    });
    return indexed_array;
}


})