from django.urls import path
from . import views

app_name='my-admin'
urlpatterns = [
    path('admin/order-detail/<int:pk>/', views.DetailOrder.as_view(), name='detail-order'),
    path('admin/order-detail-pdf/<int:pk>/', views.DetailOrderPDF.as_view(), name='detail-order-pdf')


]