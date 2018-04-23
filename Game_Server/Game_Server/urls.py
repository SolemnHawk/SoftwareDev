
from user import views 
from score import views
from django.contrib import admin
from django.urls import path
from user import views as uv
from score import views as scorev
from django.urls import path
from subscribe import views as subv

urlpatterns = [
    path('user/', uv.HomePageView().create_or_retrieve),
    path('user/<str:uname>/', uv.HomePageView().create_or_retrieve),
	path('subscribe/', subv.HomePageView().create_or_retrieve),
	path('subscribe/<str:uname>/',subv.HomePageView().create_or_retrieve),
	path('subscribe/<str:uname>/<int:subl>/',subv.HomePageView().create_or_retrieve),
    path('score/', scorev.HomePageView().create_or_retrieve),
    path('score/<str:idval>/', scorev.HomePageView().create_or_retrieve),
]
