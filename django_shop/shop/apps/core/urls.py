from django.urls import path
from . import views, api

app_name = 'core'
urlpatterns = [
    path('', views.MainPageView.as_view(), name='main-page'),
    path('products/', views.MainPageView.as_view(), name='products'),
    path('detail-product/', views.DetailProductView.as_view(), name='detail-product'),
    path('detail/<slug:slug>/', views.DetailProductView.as_view(), name='detail-product-main')
]
