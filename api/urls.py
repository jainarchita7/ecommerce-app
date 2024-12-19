from api.views import RegistrationView, ProductView, CartView
from django.urls import path

urlpatterns = [
    path('register/', RegistrationView.as_view(),
         name = 'register'),
    path('products/', ProductView.as_view(),
         name = 'products'),
    path('products/<int:pk>/', ProductView.as_view(),
         name = 'product-details'),
    path('cart/',CartView.as_view(),
         name = 'cart'),
    ]