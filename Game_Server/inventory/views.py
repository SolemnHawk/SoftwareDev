from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
import json
from inventory.models import Inventory
from django.views.decorators.csrf import csrf_exempt
import urllib.request

class HomePageView(APIView):
	@csrf_exempt
	def create_or_retrieve(self, request=None, uname="test", description="test", format=None):

            page = urllib.request.urlopen('http://localhost:8000/user/' + uname)
            json_string = page.read()
            parsed_json = json.loads(json_string)


            if request.method =="GET":
                try:
                    found_id = parsed_json['id']
                    user_id = Inventory.objects.get(id=found_id)
                except ObjectDoesNotExist as e:
                    return HttpResponse(json.dumps({"status": "NoSuchID"}), status=404)

                data = {"ID": user_id.id, "Inventory": user_id.description}
                return HttpResponse(json.dumps(data))

            elif request.method == "POST":
                try:
                    found_id = parsed_json['id']
                    user_id = Inventory.objects.get(id=found_id)
                    return HttpResponse(json.dumps({"status": "AlreadyExists"}), status=403)
                except ObjectDoesNotExist as e:
                    pass
                u = Inventory(id=found_id)
                u.save()
                return HttpResponse(json.dumps({"status": "Success"}))

            elif request.method == "PUT":
                try:
                    found_id = parsed_json['id']
                    user = Inventory.objects.get(id=found_id)
                    user.description = description
                    user.save()
                    return HttpResponse(json.dumps({"status": "Success"}))
                except ObjectDoesNotExist as e:
                    return HttpResponse(json.dumps({"status": "NoSuchUser"}))



