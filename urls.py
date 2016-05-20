from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from . import foodpanda , security
import json

@csrf_exempt
def test(request):
    if request.method == "GET":
        extra = {
            "method": "GET",
            "requestData": request.GET
        }
    else:
        extra = {
            "method": "POST",
            "requestData": json.loads(request.body.decode())
        }
    return JsonResponse({
        "result": True,
        "Message": "Welcome to the Foodpanda API",
        "extra": extra
    })

@csrf_exempt
def error404(request):
	return JsonResponse({
        "error": 404,
        "Message": "Page not found!",
    })

urlpatterns = [
#	url(r'^$', test),
	url(r'restaurant$',  security.auth(foodpanda.showVendorData)),
	url(r'sales_head$',  security.auth(foodpanda.Saleshead)),
	url(r'restaurant_data$',  security.auth(foodpanda.restaurant_portfolio)),
	url(r'am_data$',  security.auth(foodpanda.AM_portfolio)),
	url(r'city_data$',  security.auth(foodpanda.city_portfolio)),
	url(r'am$',  security.auth(foodpanda.AM)),
	url(r'city_head$',  security.auth(foodpanda.Cityhead)),
	url(r'check_email$' , security.auth(foodpanda.check_email)) ,
	url(r'/*$',error404 )
]