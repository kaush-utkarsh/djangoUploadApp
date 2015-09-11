from django.shortcuts import render,render_to_response
from django.template.context import RequestContext

def home(request):
	context = RequestContext(request,
						   {'request': request,
							'user': request.user})
	return render_to_response('login.html',
						 context_instance=context)