from django.shortcuts import render,render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore
from django.views.decorators.csrf import csrf_exempt
import traceback, time, datetime, hashlib, json, methods, requests


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
			methods.add_files(s['userid'],project.projectid,f['name'],f['link'],f['thumbnail'],f['type'],f['source'])

		resp = {"project_id":project.projectid,"project_title":project_title}

		return HttpResponse(json.dumps(resp))

def save_profile(backend, user, response, *args, **kwargs):
	if backend.name == 'facebook':
		# profile = user.get_profile()
		# if profile is None:
		# 	profile = Profile(user_id=user.id)
		# profile.gender = response.get('gender')
		# profile.link = response.get('link')
		# profile.timezone = response.get('timezone')
		print user.social_auth.get(provider='facebook').uid
		# print user.social_auth.get(provider='facebook').email
		print response
		# print profile

def user_details(backend, user, response, *args, **kwargs):
	if backend.name == 'facebook':
		# profile = user.get_profile()
		# if profile is None:
		# 	profile = Profile(user_id=user.id)
		# profile.gender = response.get('gender')
		# profile.link = response.get('link')
		# profile.timezone = response.get('timezone')
		print response
		# print profile
	if backend.name == 'google':
		# profile = user.get_profile()
		# if profile is None:
		# 	profile = Profile(user_id=user.id)
		# profile.gender = response.get('gender')
		# profile.link = response.get('link')
		# profile.timezone = response.get('timezone')
		print response['access_token']
		social = user.social_auth.get(provider='google-oauth2')
		response1 = requests.get(
			'https://www.googleapis.com/plus/v1/people/me/',
			params={'access_token': social.extra_data['access_token']}
		)
		# friends = response.json()['items']
		print response1
		print response1.json()


		# print profile

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
