
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
    path('score/', scorev.HomePageView().create_or_retrieve),
    path('score/<str:idval>/', scorev.HomePageView().create_or_retrieve),
]

'''urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', HomePageView().get),
    path('user/<str:uname>/',HomePageView().get),
    path('user/', views.index, name='index'),
    #path('user/<str:uname>/', views.get),
    path('score/',scorevHomePageView().create_or_retrieve(),
    path('score/<str:idval>/',scorev.HomePageView().create_or_retrieve(),
    path('score/', views.index, name='index'),
    #path('score/<str:idval>/', views.create_or_retrieve),
    
]'''
