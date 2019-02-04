$(document).on('click', '[data-action="delete-cart-product"]', function() {
    var id = $(this).data('id')
    $.ajax({
        url: '/cart/delete/',
        method: 'POST',
        data: {'id': id},
        success: function(data) {
            var data = data['count']
            $('[data-id="counter-product-' + id + '"]').text(data['count_order'])
            $('#cart-counter').text(data['count'])

        },

    })
})


$(document).on('click', '[data-action="delete-cart-product-all"]', function() {
    var element = $(this)
    var id = $(this).data('id')
    $.ajax({
        url: '/cart/delete-all/',
        method: 'POST',
        data: {'id': id},
        success: function(data) {
            var data = data['count']
            element.closest('[data-id="body-product-cart"]').remove()
            $('#cart-counter').text(data['count'])

        },

    })
})




