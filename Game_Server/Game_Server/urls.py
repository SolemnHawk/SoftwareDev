from user import views 
from score import views
from django.contrib import admin
from django.urls import path
from user import views as uv
from score import views as scorev
from django.urls import path

urlpatterns = [
    path('user/', uv.HomePageView().get),
    path('user/<str:uname>/', uv.HomePageView().get),
    	path('score/',scorev.HomePageView().create_or_retrieve),
    	path('score/<str:uname>/',scorev.HomePageView().create_or_retrieve),
    	path('score/<str:uname>/<str:scoreval>/', scorev.HomePageView().create_or_retrieve),
]