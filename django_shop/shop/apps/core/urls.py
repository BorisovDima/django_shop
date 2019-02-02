from django.urls import path
from . import views, api

urlpatterns = [
    path('', views.MainPage.as_view(), name='main-page'),

    path('api/detail-product/', api.DetailProductAPI.as_view({'get': 'retrieve'}), name='detail-product')

]
