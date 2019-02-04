$(document).on('click', '[data-action="order-product"]', function() {
    var id = $(this).data('id')
    $.ajax({
        url: '/cart/put/',
        method: 'POST',
        data: {'id': id},
        success: function(data) {
            var data = data['count']
            $('[data-id="counter-product-' + id + '"]').text(data['count_order'])
            $('#cart-counter').text(data['count'])
            $('#detail-product-modal').modal('hide')

        },

    })
})
