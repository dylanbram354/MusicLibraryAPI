from django.urls import path
from . import views


urlpatterns = [
    path('music/', views.SongList.as_view()),
    path('music/<int:pk>/', views.SongDetail.as_view()),
    path('music/like/<int:pk>/', views.LikeSong.as_view()),
    path('music/unlike/<int:pk>/', views.UnlikeSong.as_view())
]