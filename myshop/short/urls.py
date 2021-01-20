from django.urls import path
from .import views

app_name = 'short'

urlpatterns = [
    path('', views.make, name='make'),
    path('<str:token>', views.Home, name='Home'),
]