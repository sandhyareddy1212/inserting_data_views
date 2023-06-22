from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    tn=input('enter topic_name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic is inserted')



def insert_webpage(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('webpage is created')


def insert_AcessRecord(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    d=input('enter date')
    a=input('enter author')
    AR=AcessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AR.save()
    return HttpResponse('AcessRecord is created')

def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)

def display_acessrecords(request):
    acessrecords=AcessRecord.objects.all()
    d={'acessrecords':acessrecords}
    return render(request,'display_acessrecords.html',d)






