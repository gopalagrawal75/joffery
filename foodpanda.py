from bson.json_util import dumps
from django.views.decorators.csrf import csrf_exempt
from . import db, get_json, basic_success, basic_error

failure = dumps({"Failed"})
@csrf_exempt
def showVendorData(request):
	try:
		code = request.GET['vendor_code']
	except:
		return basic_error("invalid parameters")
		
	try:
		data={}
		restaurant = db.restaurant_data
		data['info']=restaurant.find_one({"vendor_code":code} , {"_id":False})
		sales = db.sales
		data['sales']=sales.find_one({"vendor_code":code} , {"_id":False})
		week4=db.ops_data_4_week
		data['week4']=week4.find_one({"vendor_code":code} , {"_id":False})
		weekly = db.ops_data_weekly
		data['weekly']=weekly.find({"vendor_code":code} , {"_id":False})
		log=db.log_data
		data['logs']=log.find_one({"vendor_code":code} , {"_id":False})
		action = db.action_board
		data['action']=action.find({"vendor_code":code} , {"_id":False})
		return basic_success(data)
	except Exception as e:
		return basic_error(e)

