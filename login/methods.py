import urllib2
import datetime,time
import json
from .models import User_Details
from django.template import Context, Template, loader
from django.core import serializers

def get_user(username):
	user = ''
	try:
		user = User_Details.objects.get(username = username)
	except User_Details.DoesNotExist:
		user = []
		return user
		# pass
		# return serializers.serialize("json", user.objects.all())	        
	return serializers.serialize("json", [user])

def create_user(name,email,username,hash_pwd):
	user= User_Details(name=name, email=email, username = username,password=hash_pwd)
	user.save()
	return user

def get_project(userid,project):
	project = ''
	try:
		project = Project_Table.objects.get(project_title = project,userid=userid)
	except Project_Table.DoesNotExist:
		project = []
		return project
		# pass
		# return serializers.serialize("json", user.objects.all())	        
	return serializers.serialize("json", [project])

# def create_project(name,email,username,hash_pwd):
# 	user= User_Details(name=name, email=email, username = username,password=hash_pwd)
# 	user.save()
# 	return user