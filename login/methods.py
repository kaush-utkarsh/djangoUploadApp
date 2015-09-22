import urllib2
import datetime,time
import json
from .models import *
from django.template import Context, Template, loader
from django.core import serializers

def get_user(username):
	user = ''
	try:
		user = User_Details.objects.get(username = username)
	except User_Details.DoesNotExist:
		user = []
		return user
	return serializers.serialize("json", [user])

def create_user(name,email,username,hash_pwd):
	user= User_Details(name=name, email=email, username = username,password=hash_pwd)
	user.save()
	return user

def get_social_user(userid,source):
	user = ''
	try:
		if source is 'facebook':
			user = User_Details.objects.get(facebook_id = userid)
		else:
			user = User_Details.objects.get(google_id = userid)
	except User_Details.DoesNotExist:
		user = []
		return user
	return serializers.serialize("json", [user])

def create_social_user(name,source,userid):
	if source is 'facebook':
		user= User_Details(name=name, facebook_id = userid)
	else:
		user= User_Details(name=name, google_id = userid)
	user.save()
	return user

def upload_video(name, userid):
	upload = Uploaded_File_Table(upload_field=name, userid=userid)
	upload.save()
	return upload.upload_id

def get_project(userid,project):
	project = ''
	try:
		project = Project_Table.objects.get(project_title = project,userid=userid)
	except Project_Table.DoesNotExist:
		project = []
		return project
	return serializers.serialize("json", [project])

def create_project(userid,project_title,project_instructions):
	project= Project_Table(userid=userid, project_title=project_title, project_instructions = project_instructions)
	project.save()
	return project

def add_files(userid,projectid,name,link,server,thumbnail,ftype,source):
	nFile= User_File_Table(userid=userid, projectid=projectid, file_title = name, file_web_path = link, file_server_path = server, file_thumbnail_path =thumbnail, file_type = ftype,file_source_type =source )
	nFile.save()
	return nFile
