
def static_version(req):

    static = {'post_ajax_js': "core/js/post_ajax.js?v=1",
              'detail_product_js': "core/js/detail-product.js?v=1",
              'load_products_js': "core/js/load-products.js?v=2",
              'delete_from_cart_js': "cart/js/delete-from-cart.js?v=1",
              'check_cart_js': "cart/js/check_cart.js?v=1",
              'put_in_cart_product_js': "cart/js/put-in-cart-product.js?v=1",
              'order_css': "order/css/order.css?v=1"}

    return static


