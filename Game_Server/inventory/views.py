from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
import json
from inventory.models import Inventory
from django.views.decorators.csrf import csrf_exempt

class HomePageView(APIView):
	@csrf_exempt
	def create_or_retrieve(self, request=None, uid=0, format=None):
            if request.method =="GET":
                try:
                    found_id = Inventory.objects.get(id=uid)
                except ObjectDoesNotExist as e:
                    return HttpResponse(json.dumps({"status": "NoSuchID"}), status=404)

                data = {"ID": uid, "Inventory": found_id.description}
                return HttpResponse(json.dumps(data))

            elif request.method == "POST":
                try:
                    found_id = Inventory.objects.get(id=uid)
                    return HttpResponse(json.dumps({"status": "AlreadyExists"}), status=403)
                except ObjectDoesNotExist as e:
                    pass
                u = Inventory(id=uid)
                u.save()
                return HttpResponse(json.dumps({"status": "Success"}))


