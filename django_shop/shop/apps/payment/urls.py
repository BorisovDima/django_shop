from django.urls import path
from . import views

urlpatterns = [
    path('paypal/', views.PaymentProcess),
    path('done/', views.PaymentDone),
    path('cancel/', views.PaymentCanceled)
]