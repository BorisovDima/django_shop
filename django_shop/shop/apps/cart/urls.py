from django.urls import path
from . import views

urlpatterns = [
    path('put/', views.CartView.as_view({'post': 'put_order'}, event='add'), name='put-in-cart'),
    path('delete/', views.CartView.as_view({'post': 'put_order'}, event='delete'), name='delete-from-cart'),
    path('check/', views.CartView.as_view({'get': 'list'}), name='check-cart')
]