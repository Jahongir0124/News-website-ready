from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.template import loader
from .foms import *
def index(request):
    return HttpResponse("kjuinjmnjjjkmjkmjmjm")
def info(request):
    info_list=Info.objects.all()
  
    template = loader.get_template("news/info.html")
    context = {'info_list': info_list,}
    return HttpResponse(template.render(context, request))
def info1(request,info_id):
    info_list=Info.objects.filter(id=info_id)

    template=loader.get_template("news/getInfo.html")
    context={
        'info_list':info_list,
    }
    return HttpResponse(template.render(context,request))
def add_info(request):
    form=Form()
    form1= Form(request.POST)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'news/info_add.html', context)

def get_tag(request):
    category = Category.objects.all()
    template=loader.get_template("news/categories.html")
    context={
        'tag_info':category,
    }
    return HttpResponse(template.render(context, request))
def category(request,tag_id):
    tag_info = Info.objects.filter(cat_name_id=tag_id)
    template = loader.get_template("news/info.html")
    context = {'info_list': tag_info,}
    return HttpResponse(template.render(context, request))
def tag_info(request,tag_name,info_id):
    info_list = Info.objects.filter(id=info_id)
    template = loader.get_template("news/info1.html")
    context = {
        'info_list': info_list,
    }
    return HttpResponse(template.render(context, request))

def about_page(request):
    return render(request,'news/about.html')
def akk(request):
    pass
