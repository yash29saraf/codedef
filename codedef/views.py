from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

def intro(request):
    return render(request,'intro.html',{})
    