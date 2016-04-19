from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from . import foodpanda
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

urlpatterns = [
    url(r'^$', test),
    url(r'restaurant$',  foodpanda.showVendorData),
	url(r'sales_head$',  foodpanda.Saleshead),
	url(r'restaurant_data$',  foodpanda.restaurant_portfolio),
	url(r'am_data$',  foodpanda.AM_portfolio),
	url(r'city_data$',  foodpanda.city_portfolio),
	url(r'am$',  foodpanda.AM),
	url(r'city_head$',  foodpanda.Cityhead),
	
    
]



