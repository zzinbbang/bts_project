from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('event/', views.event, name='event'),
    path('check/', views.check, name='check')
]