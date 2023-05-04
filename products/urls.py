from django.urls import path
from .views import ProductListView, ProductDetailView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', ProductListView.as_view()), #this handles products
    path('<int:pk>/', ProductDetailView.as_view()) #Handles products/pk
]
