from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
import json
from subscribe.models import Subscribe
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


class HomePageView(APIView):
	@csrf_exempt
	def create_or_retrieve(self, request=None, uid="test", format=None):
		if request.method == "GET":
			try:
				found_id = Subscribe.objects.get(id = uid)
			except ObjectDoesNotExist as e:
				return HttpResponse(json.dumps({"status":"NoSuchID"}),status = 404)
			
			data = {"id":found_id.id, "level":found_id.level}
			return HttpResponse(json.dumps(data),status = 200)
		elif request.method == "POST":
			try:
				found_id = Subscribe.objects.get(id = uid)
				return HttpResponse(json.dumps({"status":"AlreadyExists"}),status=403)
			except ObjectDoesNotExist as e:
				pass
			u = Subscribe(id = uid)
			u.save()
			return HttpResponse(json.dumps({"status":"Success"}))
			
			