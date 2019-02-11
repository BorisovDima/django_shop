$(document).on('click', '[data-action="delete-cart-product"]', function() {
    var element = $(this).closest('[data-id="body-product-cart"]')
    var id = $(this).data('id')
    $.ajax({
        url: '/cart/delete/',
        method: 'POST',
        data: {'id': id},
        success: function(data) {
            var data = data['count']

            element.find('[data-id="cart-counter-product"]').text(data['count_order'])
            element.find('[data-id="cart-variant-price"]').text(data['price'])

            $('#cart-counter').text(data['count'])

        },

    })
})


$(document).on('click', '[data-action="delete-cart-product-all"]', function() {
    var element = $(this).closest('[data-id="body-product-cart"]')
    var id = $(this).data('id')
    $.ajax({
        url: '/cart/delete-all/',
        method: 'POST',
        data: {'id': id},
        success: function(data) {
            var data = data['count']
            element.remove()
            $('#cart-counter').text(data['count'])
        },

    })
})




