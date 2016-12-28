from django.conf.urls import include, url

import scrapers.views

urlpatterns = [
    url(r'^$', 					scrapers.views.headlines, name='headlines'),
    url(r'^headlines', 			scrapers.views.headlines, name='headlines'),
    url(r'^deadpeoplenews', 	scrapers.views.deadpeoplenews, name='deadpeoplenews'),
    url(r'^feedkeys', 			scrapers.views.feedkeys, name='feedkeys'),
]
