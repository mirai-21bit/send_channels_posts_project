from django.urls import path
from . import views


app_name = 'custom_admin'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_channel/', views.add_channel, name='add_channel'),
]