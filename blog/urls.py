from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^hello/','blog.views.hello',name='hello'),
)
