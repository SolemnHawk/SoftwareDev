from django.shortcuts import render
from django.http import HttpResponse
#from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
import json
#from user import models

# Create your views here.
'''class HomePageView(APIView):
    def get(self, request=None, uname="test", format=None):
        data = { "user": uname, "key2": "value2" }
        return HttpResponse(json.dumps(data))'''


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the user index.")





def get(request=None, uname="test", format=None):
    try:
        found_user = User.objects.get(name=uname)
    except ObjectDoesNotExist as e:
        return HttpResponse(json.dumps({"status":"NoSuchUser"}), status=404)

    data = { "user": uname, "id": found_user.id}
    return HttpResponse(json.dumps(data))
