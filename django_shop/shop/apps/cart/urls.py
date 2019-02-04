from django.urls import path
from . import views

urlpatterns = [
    path('put/', views.CartView.as_view(event='add', render_key='count'), name='put-in-cart'),
    path('delete/', views.CartView.as_view(event='delete', render_key='count'), name='delete-from-cart'),
    path('delete-all/', views.CartView.as_view(event='delete_all', render_key='count'), name='delete-from-cart-all'),
    path('check/', views.CartView.as_view(render_template='cart/objects/cart_object.html'), name='check-cart')
]