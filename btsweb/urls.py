from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('event/', views.event, name='event'),
    # path('check/', views.check, name='check')
    path('confirm/', views.confirm, name='confirm'),
    path('check/', views.check, name='check'),
    path('detail/', views.detail, name='detail'),
    path('cancelpage/', views.cancelpage, name='cancelpage'),
    path('delete/<usercode>', views.delete, name='delete'),
    path('sign/', views.sign, name='sign'),
]