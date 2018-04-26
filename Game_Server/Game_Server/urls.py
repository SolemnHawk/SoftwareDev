
from user import views
from inventory import views
from django.contrib import admin
from django.urls import path
from user import views as uv
from inventory import views as inuv
from django.urls import path

urlpatterns = [
    path('user/', uv.HomePageView().create_or_retrieve),
    path('user/<str:uname>/', uv.HomePageView().create_or_retrieve),
    path('inventory/', inuv.HomePageView().create_or_retrieve),
    path('inventory/<str:uname>/',inuv.HomePageView().create_or_retrieve),
    path('inventory/<str:uname>/<str:description>/',inuv.HomePageView().create_or_retrieve),
]

