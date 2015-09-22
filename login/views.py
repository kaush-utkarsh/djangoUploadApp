from django.shortcuts import render,render_to_response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.template.context import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore
from django.views.decorators.csrf import csrf_exempt
import traceback, time, datetime, hashlib, json, methods, requests, os, string
from WeEdit import settings


s = SessionStore()
		
def home(request):
	if 'username' in s.keys():
		if s['username'] != '':
			data = {'username': s['username']}
			return render(request, "base.html", data)

	context = RequestContext(request,
						   {'request': request,
							'user': request.user})
	return render_to_response('login.html',
						 context_instance=context)


def dashboard(request):
	if 'username' in s.keys():
		if s['username'] != '':
			data = {'username': s['username']}
			return render(request, "dashboard.html", data)

	context = RequestContext(request,
						   {'request': request,
							'user': request.user})
	return HttpResponseRedirect("/")

def checkout(request):
	if 'username' in s.keys():
		if s['username'] != '':
			data = {'username': s['username']}
			return render(request, "payment.html", data)

	context = RequestContext(request,
						   {'request': request,
							'user': request.user})
	return HttpResponseRedirect("/")

def new_project(request):
	if 'username' in s.keys():
		if s['username'] != '':
			data = {'username': s['username']}
			return render(request, "create_project.html", data)

	context = RequestContext(request,
						   {'request': request,
							'user': request.user})
	return HttpResponseRedirect("/")



def signIn(request):
	if request.method == 'POST':
		username = request.POST.get('form-username', '')
		password = request.POST.get('form-password','')
		hash_pwd = hashlib.md5(password).hexdigest()
		user = ''
		user = methods.get_user(username)
		if len(user) == 0:
			resp = "false"
		else:
			u = json.loads(user)
			print hash_pwd
			print u[0]['fields']['password']
			if hash_pwd == u[0]['fields']['password']:
				resp = username
				s['username'] = username
				s['userid'] = u[0]['pk']
				s.save()
			else:
				resp = "false"
		return HttpResponse(resp)


@csrf_exempt
def create_project(request):
	if request.method == 'POST':
		project_title = request.POST.get('projectTitle', '')
		instructions = request.POST.get('instructions')
		files = request.POST.get('files', '')
		print project_title
		print instructions
		projects = methods.get_project(s['userid'],project_title)
		if len(projects) != 0:
			project_title = project_title + str(len(projects)+1)
		
		project = methods.create_project(s['userid'],project_title,instructions)
		
		for f in json.loads(files):
			methods.add_files(s['userid'],project.projectid,f['name'],f['link'],'',f['thumbnail'],f['type'],f['source'])

		resp = {"project_id":project.projectid,"project_title":project_title}
		s['current_project'] = project.projectid
		return HttpResponse(json.dumps(resp))

@csrf_exempt
def upload_video_file(request):
	resp = {"success":[]}
	userid = s['userid']
	projectid = s['current_project']
	if request.method == 'POST':
		print request.FILES
		upfile = request.FILES.getlist('my_file')
		print upfile
		for data in upfile:
			print data
			current_timestamp = string.replace(string.replace(string.replace(string.replace(str(datetime.datetime.now()),' ',''),'.',''),':',''),'-','')
			path = default_storage.save(current_timestamp, ContentFile(data.read()))
			tmp_file = os.path.join(settings.MEDIA_ROOT, path)
			methods.add_files(userid,projectid,data.name,'',tmp_file,'','video','local upload')
			# id = methods.upload_video(timezonemp_file, userid)
			# resp["success"].append(id)
			resp = "dsad"
	return HttpResponse(json.dumps(resp))


@csrf_exempt
def upload_audio_file(request):
	resp = {"success":[]}
	userid = s['userid']
	projectid = s['current_project']
	if request.method == 'POST':
		print request.FILES
		upfile = request.FILES.getlist('my_file')
		print upfile
		for data in upfile:
			print data
			current_timestamp = string.replace(string.replace(string.replace(string.replace(str(datetime.datetime.now()),' ',''),'.',''),':',''),'-','')
			path = default_storage.save(current_timestamp, ContentFile(data.read()))
			tmp_file = os.path.join(settings.MEDIA_ROOT, path)
			methods.add_files(userid,projectid,data.name,'',tmp_file,'','audio','local upload')
			# id = methods.upload_video(timezonemp_file, userid)
			# resp["success"].append(id)
			resp = "dsad"
	return HttpResponse(json.dumps(resp))


def save_profile(backend, user, response, *args, **kwargs):
	if backend.name == 'facebook':
		name = 'name'
		social = 'facebook'		
	else:
		name = 'displayName'
		social = 'google'		

	u = methods.get_social_user(response['id'],social)
	
	if len(u) != 0:
		u1 = json.loads(u)
		s['username'] = response[name]
		s['userid'] = u1[0]['pk']
		s.save()
	else:
		u = methods.create_social_user(response[name],social,response['id'])
		s['username'] = response[name]
		s['userid'] = u.userid
		s.save()

def signUp(request):
	if request.method == 'POST':
		username = request.POST.get('form-username', '')
		name = request.POST.get('form-name','')
		email = request.POST.get('form-email','')
		password = request.POST.get('form-password','')
		hash_pwd = hashlib.md5(password).hexdigest()
		user = ''
		user = methods.get_user(username)
		if len(user) != 0:
			resp = "false"
		else:
			user = methods.create_user(name,email,username,hash_pwd)
			s['username'] = username
			s['userid'] = user.userid
			s.save()
			resp = username
		return HttpResponse(resp)

@csrf_exempt
def signOut(request):
	if request.method == 'POST':
		s['username'] = ''
		s.save()

		return HttpResponse("success")
