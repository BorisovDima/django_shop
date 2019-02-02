$('[data-action="detail-product"]').on('click', function() {
    $.ajax({
        url: '/api/detail-product/',
        method: 'GET',
        data: {'pk': $(this).data('id')},
        success: function(context) {
              var source = $("#detail-template").html()
              var template = Handlebars.compile(source)
              var html = template(context)
              $("#base-shop-modal").html(html)
              $('#base-shop-modal').modal('show')
        },
        error: function(data) {
            console.log('Invalid')
        },
    })

})


$('#base-shop-modal').on('hide.bs.modal', function() {
    $("#base-shop-modal").html('')
})

