from django.shortcuts import render,render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore
from django.views.decorators.csrf import csrf_exempt
import traceback, time, datetime, hashlib, json, methods

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
				s.save()
			else:
				resp = "false"
		return HttpResponse(resp)

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
			methods.create_user(name,email,username,hash_pwd)
			s['username'] = username
			s.save()
			resp = username
		return HttpResponse(resp)

@csrf_exempt
def signOut(request):
	if request.method == 'POST':
		s['username'] = ''
		s.save()

		return HttpResponse("success")
