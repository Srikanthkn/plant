from django.contrib import admin

# Register your models here.
from donation.models import userlogin

class userloginAdmin(admin.ModelAdmin):
     list_display=[ 'id','firstname','lastname','mobilenumber']


admin.site.register(userlogin)