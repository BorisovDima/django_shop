$(document).on('click', '[data-action="order-product"]', function() {
    $.ajax({
        url: '/cart/put/',
        method: 'POST',
        data: {'id': $(this).data('id')},
        success: function(data) {
            $('#cart-counter').text(data['count'])
            $('#detail-product-modal').modal('hide')
        },

    })
})
