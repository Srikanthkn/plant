from django.urls import path
from sellandbuy.views import sellplant1;
from sellandbuy.views import buyplant;
from sellandbuy.views import donatemoney;



urlpatterns = [
    
    path('sell/',sellplant1),
    path('buy/',buyplant),
    path('donatemoney/', donatemoney ),

]
