from django.shortcuts import render_to_response,render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from forms import KnowledgeForm

def yourself(request):
	if request.POST:
		form = KnowledgeForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/recorded/')
	else:
		form = KnowledgeForm()	
	args={}
	args['form']=form
	return render(request,'yourself.html',args)

def recorded(request):
    return render(request,'recorded.html',{})

def contacts(request):
    return render(request,'contacts.html',{})