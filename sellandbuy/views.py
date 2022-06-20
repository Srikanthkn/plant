from django.shortcuts import render


# Create your views here.
def sellplant1(request):
  return  render(request,'sellandbuy/sellplant1.html')
  

def buyplant(request):
      
     return  render(request,'sellandbuy/buyplant.html')

def donatemoney(request):
       
   return  render(request,'sellandbuy/donatemoney.html')