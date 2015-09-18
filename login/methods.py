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

def add_files(userid,projectid,name,link,thumbnail,ftype,source):
	nFile= User_File_Table(userid=userid, projectid=projectid, file_title = name, file_web_path = link, file_thumbnail_path =thumbnail, file_type = ftype,file_source_type =source )
	nFile.save()
	return nFile
