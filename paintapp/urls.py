from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
        (r'^$', 'paint.views.index'),
	(r'^redirect$', 'paint.views.load'),
	(r'^redirect$', 'paint.views.loads'),
       
#(r'^statics/(?P<path>.*)$', 'django.views.static.serve',
 #       {'document_root': settings.STATIC_DOC_ROOT}),
        (r'^admin/', include(admin.site.urls))
        )
	

