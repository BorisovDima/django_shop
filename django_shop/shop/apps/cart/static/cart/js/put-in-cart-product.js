$(document).on('click', '[data-action="order-product"]', function() {
    var id = $(this).data('id')
    var element = $(this)
    $.ajax({
        url: '/cart/put/',
        method: 'POST',
        data: {'id': id},
        success: function(data) {
            var data = data['count']
            $('[data-id="counter-product-' + id + '"]').text(data['count_order'])
            $('#cart-counter').text(data['count'])
            $('#base-shop-modal').modal('hide')
            console.log(data['extra'])
            if (data['extra']) {
                element.closest('[data-id="body-product-cart"]').append('WARNING!')
            }
        },

    })
})
