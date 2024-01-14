from tuneTracker import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('artists/', views.artists, name="artists"),
    path('add-artist/', views.add_artist, name='add-artist'),
    path('add-song/', views.add_song, name='add-song'),
    path('contact/', views.contact, name='contact'),
]
