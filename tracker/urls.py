from django.urls import path
from . import views

urlpatterns = [
    path('', views.watchlist_list, name='watchlist_list'),
    path('watchlist/<int:pk>/', views.watchlist_detail, name='watchlist_detail'),
    path('add/', views.add_watchlist, name='add_watchlist'),
    path('watchlist/<int:watchlist_id>/add_item/', views.add_item, name='add_item'),
    path('register/', views.register, name='register'),
]
