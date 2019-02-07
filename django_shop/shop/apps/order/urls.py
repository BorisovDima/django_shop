from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('order/', views.OrderView.as_view(), name='form-order'),
    path('order/payment/', views.OrderPaymentPageView.as_view(), name='order-pay-page'),
]
