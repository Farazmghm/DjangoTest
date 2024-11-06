from django.shortcuts import render
import datetime
from django.conf import settings
from .models import Faraz,Post
from django.http import Http404,HttpResponseRedirect
from .form import Form1,Form2
from django.urls import reverse


def index(request):
    context={
          "name":"faraz",
          "family":"moghaddam",
          "age":34,
          "Name":range(20),
          "list1":["ali","mohammad","hassan","hossein"],
          "row":range(5),
          "col":range(6),
          
               
        
            }
    return render(request,'mainapp/index.html',context)



def step1(request):
    today=datetime.datetime.now
    context={
        "today":today,
        "tag": "<h1> farazmoghaddam<h1>"
           }
    
    return render(request,'mainapp/page1.html',context)


def step2(request):
    context={'name':'faraz',
             'age':34
             
             }
    return render(request,'mainapp/page2.html',context)

import os
def step4(request):
    img=os.listdir(settings.MEDIA_ROOT+'/images')
    
    context={
        
        'media_url':settings.MEDIA_URL,
        'img':img
 
            }
    return render(request,'mainapp/page4.html',context)


def step5(request):
    faraz=Faraz.objects.all()
    context={
        'faraz':faraz
    }
    return render(request,'mainapp/page5.html',context)


def step7(request):
    faraz=Faraz.objects.all()
  
    context={
        
        'media':settings.MEDIA_URL,
         'faraz':faraz,}
  
    return render(request,'mainapp/page7.html',context)


def detail(request,id_feild):
    try:
          de=Faraz.objects.get(id=id_feild)
    except Faraz.DoesNotExist :
        raise Http404("This Page Not Fund")
    context={
        'media':settings.MEDIA_URL,
        'de':de
        
    }
    return render(request,'mainapp/detail.html',context)


def form1(request):
    context={}
    if request.method=='POST':
        form=Form1(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data['name'],data['family'],data['age'])
        else:
            context["error_messag"]="Form Is Not Valid..."
    else:
        form=Form1()
    context['form']=form
    return render(request,'mainapp/form1.html',context)

def form2(request):
    context={}
    form=Form2(request.POST)
    if form.is_valid():
        data=form.cleaned_data
        post=Post()
        post.name=data['name']
        post.family=data['family']
        post.age=data['age']
        post.is_active=data['is_active']
        post.save()
        return HttpResponseRedirect(reverse('index'))
    context={
        'form':form
    }
    return render(request,'mainapp/form2.html',context)

def render1(request):
   
    return HttpResponseRedirect(request,'mainapp/thank.html')
    