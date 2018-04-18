
from user import views 
from django.contrib import admin
from django.urls import path
from user import views as uv
from django.urls import path
from subscribe import views
from subscribe import views as subv

urlpatterns = [
    path('user/', uv.HomePageView().get),
    path('user/<str:uname>/', uv.HomePageView().get),
	path('subscribe/', subv.HomePageView().create_or_retrieve),
	path('subscribe/<str:uid>/',subv.HomePageView().create_or_retrieve),
]

'''urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', HomePageView().get),
    path('user/<str:uname>/',HomePageView().get),
    path('user/', views.index, name='index'),
    #path('user/<str:uname>/', views.get),
	path('subscribe/' subv.HomePageView().get),
	path('subscribe/<str:uid>/', subv.HomePageView().get),
]'''
