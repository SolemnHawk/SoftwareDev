from user import views 
from score import views
from django.contrib import admin
from django.urls import path
from user import views as uv
from score import views as scorev
from user import views
from inventory import views
from django.contrib import admin
from django.urls import path
from user import views as uv
from inventory import views as inuv
from subscribe import views as subv

urlpatterns = [
    path('user/', uv.HomePageView().create_or_retrieve),
    path('user/<str:uname>/', uv.HomePageView().create_or_retrieve),
	path('subscribe/', subv.HomePageView().create_or_retrieve),
	path('subscribe/<str:uname>/',subv.HomePageView().create_or_retrieve),
	path('subscribe/<str:uname>/<int:subl>/',subv.HomePageView().create_or_retrieve),
    path('score/', scorev.HomePageView().create_or_retrieve),
    path('score/<str:idval>/', scorev.HomePageView().create_or_retrieve),
    path('user/', uv.HomePageView().get),
    path('user/<str:uname>/', uv.HomePageView().get),
    path('inventory/', inuv.HomePageView().create_or_retrieve),
    path('inventory/<str:uid>/',inuv.HomePageView().create_or_retrieve),
]
