$('#my-cart').on('click', function(){
        $.ajax({
            url: '/cart/check/',
            method: 'GET',
            success: function(context) {
              var source = $("#list-my-cart").html()
              console.log(source)
              var template = Handlebars.compile(source)
              var html = template(context)
              console.log(html)
              $("#my-cart-modal").html(html)
              $('#my-cart-modal').modal('show')
            },

        })


})


$('#my-cart-modal').on('hide.bs.modal', function() {
    $("#my-cart-modal").html('')
})
