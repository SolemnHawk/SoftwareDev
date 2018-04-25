from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
import json
from score.models import Score
from django.views.decorators.csrf import csrf_exempt
import urllib.request

# Create your views here.
class HomePageView(APIView):
    @csrf_exempt
    def create_or_retrieve(self, request=None, uname="test",scoreval="0", format=None):
        page=urllib.request.urlopen('http://localhost:8000/user/'+uname)
        json_string=page.read()
        parsed_json=json.loads(json_string)

        if request.method =="GET":
            try:
		   
                    found_id = parsed_json['id']
                    user_id=Score.objects.get(id=found_id)
            except ObjectDoesNotExist as e:
                    return HttpResponse(json.dumps({"status":"NoSuchUser"}), status=404)

            data = { "ID": user_id.id, "Score": user_id.score }
            return HttpResponse(json.dumps(data))

        elif request.method == "POST":
            try:
                    found_id=parsed_json['id']
                    user_id = Score.objects.get(id=found_id)
                    return HttpResponse(json.dumps({"status":"AlreadyExists"}), status=403)
            except ObjectDoesNotExist as e:
                pass
            u = Score(id=found_id)
            u.save()
            return HttpResponse(json.dumps({"status":"Success"}))

        elif request.method =="PUT":
            try:
                found_id=parsed_json['id']
                user=Score.objects.get(id=found_id)
                user.score=scoreval
                user.save()
                return HttpResponse(json.dumps({"status":"Success"}))
            except ObjectDoesNotExist as e:
                return HttpResponse(json.dumps({"status":"NoSuchUser"}))