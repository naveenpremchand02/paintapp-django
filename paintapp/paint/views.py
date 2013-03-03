from django.template import RequestContext
from django.template.loader import get_template

from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponsePermanentRedirect

import random
import json
import string

from django import shortcuts
from url.models import Data
from django.views.decorators.csrf import csrf_exempt



def index(request):
	 s = get_template('index2.html.html')
         html = h.render(Context({}))
	 return HttpResponse(html)


@csrf_exempt
def load(request):
	fname = request.POST['fname']
	wholedata=request.POST['whole_data']
	s=Data(name=imgname,data=wholedata)
	s.save()


def loads(request):
	fnames = request.POST['fnames']
	s = get_template('index2.html')
        html = s.render(Context({}))
	p=Data.objects.filter(name=fnames)
	if p:
		 html="""<script>var data=JSON.parse(' """+p[0].wholedata+""" ');</script>"""+html
		
		
	else:
		return shortcuts.render_to_response('index3.html',tup)


