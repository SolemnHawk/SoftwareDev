
from user import views 
from django.contrib import admin
from django.urls import path
from user import views as uv
from django.urls import path

urlpatterns = [
    path('user/', uv.HomePageView().get),
    path('user/<str:uname>/', uv.HomePageView().get),
]

'''urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', HomePageView().get),
    path('user/<str:uname>/',HomePageView().get),
    path('user/', views.index, name='index'),
    #path('user/<str:uname>/', views.get),
]'''
