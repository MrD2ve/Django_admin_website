from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    # path('/home',home_page, name='home_page'),
]