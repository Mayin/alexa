from django.http import HttpResponse

import feedparser
import requests

def index(request):
    return HttpResponse('Hello Mario!')

def headlines(request):	
    page = feedparser.parse('http://feeds.reuters.com/reuters/peoplenews/.rss')

    headlines = []
    for headline in page['items']:
    	if "dies" in headline['title']:
    	    headlines.append(headline['title'] + '.<br><br>')
    return HttpResponse(headlines)

def deadpeoplenews(request):	
    page = feedparser.parse('http://feeds.reuters.com/reuters/peoplenews/.rss')

    deadpeoplenews = []
    for headline in page['items']:
    	if "dies" in headline['title']:
    	    deadpeoplenews.append(
    	    	headline['title'] + '.<br>' + 
    	    	headline['description'].split("- ",1)[1] + '<br>' +
#    	    	headline['pubDate'] + '<br>' +

    	    	'<br>')
    return HttpResponse(deadpeoplenews)

def feedkeys(request):	
    page = feedparser.parse('http://feeds.reuters.com/reuters/peoplenews/.rss')

    feedkeys = page.keys()
    return HttpResponse(feedkeys)