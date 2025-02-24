from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('capsules/', views.capsules, name='capsules'),
    path('letters/', views.letters, name='letters'),
    path('form/', views.form, name='form'),
]