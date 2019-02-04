$(document).on('click', '[data-action="detail-product"]', function() {
    $.ajax({
        url: '/detail-product/',
        method: 'GET',
        data: {'pk': $(this).data('id')},
        success: function(json) {
              $("#base-shop-modal").html(json['html'])
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

