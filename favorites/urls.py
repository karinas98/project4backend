from django.urls import path
from .views import FavoriteListView, FavoriteDetailView

urlpatterns = [
    path('', FavoriteListView.as_view()),
    path('<int:pk>/', FavoriteDetailView.as_view()),
]