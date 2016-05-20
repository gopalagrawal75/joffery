from django.views.decorators.csrf import csrf_exempt
from bson.json_util import ObjectId
from . import db, get_json, basic_failure, basic_error, basic_success
import requests
@csrf_exempt
def auth(handler):
	""" Authorization layer for Seller application
	:param handler: A function which will take 2 parameters (options, email_id) and return JSON response
	:return: the handler function wrapped with the authorization middleware
	"""
	@csrf_exempt
	def authorized_access(request):
		if request.method == "GET":
			opts = request.GET.copy()
		else:
			opts = get_json(request)
		if opts.get("access_token"):
			at = opts.get('access_token')
			res = requests.get("https://www.googleapis.com/oauth2/v1/userinfo?access_token="+at)
		else:
			return basic_error("Access Token missing, unauthorized access")
		if res.status_code is 200:
			try:
				res_data = res.json()
				try:
					if res_data.get("email"):
						email=res_data.get("email")
						return handler(opts , email , request.method)
					else:
						return basic_error("Invalid Login")	
				except Exception as e:
						return basic_error("Handler error: "+str(e))
			except Exception as e:
				return basic_error(str(e))
		else:
			return basic_error("Invalid Login")
	return authorized_access
