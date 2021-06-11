from django.urls import path
from .views import hallo

app_name= 'hallo'

urlpatterns = [
    path('',hallo,name='hallo'),
]