from unittest import result
from django.http import HttpResponse
from django.shortcuts import render

from donation.models import userlogin
from donation.forms import userloginModelForm

# Create your views here.


def homepage(request):
       return render(request,'index.html')


def login1(request):
  #get all records from the table#
  
  return render(request,'donation/login1.html');

def register(request,):
      result=userlogin.objects.all();
  # store it in one dictionary#   
      return render (request,'donation/register.html');  

def buyitem(request):
       #get all records from the table#
  
  return render(request,'donation/buyitem.html');

def donatemoney(request):
       return render (request,'donation/donatemoney.html');


            
             
