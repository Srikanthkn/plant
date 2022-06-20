from django.urls import path
from donation.views import login1
from donation.views import register
from donation.views import buyitem
from donation.views import donatemoney

urlpatterns = [
   
 path('login/',login1 ),
 path('donatemoney/',donatemoney),
    
path('register/',register ),
path('buyitem/',buyitem ),
]

