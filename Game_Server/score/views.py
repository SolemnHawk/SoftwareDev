from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
import json
from score.models import Score
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class HomePageView(APIView):
    @csrf_exempt
    def create_or_retrieve(self, request=None, idval="001", format=None):
        if request.method =="GET":
            try:
                    found_id = Score.objects.get(id=idval)
            except ObjectDoesNotExist as e:
                    return HttpResponse(json.dumps({"status":"NoSuchUser"}), status=404)

            data = { "ID": idval, "Score": found_id.score }
            return HttpResponse(json.dumps(data))
        elif request.method == "POST":
            try:
                found_id = Score.objects.get(id=idval)
                return HttpResponse(json.dumps({"status":"AlreadyExists"}), status=403)
            except ObjectDoesNotExist as e:
                pass
            u = Score(id=idval)
            u.save()
            return HttpResponse(json.dumps({"status":"Success"}))