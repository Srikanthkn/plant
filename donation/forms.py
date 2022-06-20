from django import forms
from donation.models import userlogin

class userloginModelForm(forms.ModelForm):
     class Meta:
          model = userlogin
          fields ='__all__'  
             
             
