from django.shortcuts import render
from django.http import HttpResponse
#from rest_framework.views import APIView
import json

# Create your views here.
'''class HomePageView(APIView):
    def get(self, request=None, uname="test", format=None):
        data = { "user": uname, "key2": "value2" }
        return HttpResponse(json.dumps(data))'''


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the user index.")

    
def get(self, request=None, uname="test", format=None):
        data = { "user": uname, "key2": "value2" }
        return HttpResponse(json.dumps(data))