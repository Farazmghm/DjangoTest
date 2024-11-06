from typing import Any
from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.core import validators
from .models import Post


def agevalidate(value):
    value=int(value)
    if value<18 or value>60:
        raise forms.ValidationError("out Of The Range...")
    
def namevalidate(value):
    value=str(value)
    if len(value)<3 or len(value)>8:
        raise forms.ValidationError("It Is Not Expected...")    
    


class Form1(forms.Form):
    name=forms.CharField(max_length=30,required=True,label="Name",widget=forms.TextInput(attrs={'placeholder':'faraz'}),validators=[namevalidate])
    family=forms.CharField(max_length=30,required=True,label="Family",widget=forms.TextInput(attrs={'placeholder':'Moghaddam'}))
    age=forms.IntegerField(required=False,label="AGE",validators=[agevalidate])
    # is_active=forms.BooleanField(initial=True)
    # register=forms.DateField(widget=forms.SelectDateWidget,initial=datetime.datetime.today)
    # password=forms.CharField(max_length=20,widget=forms.PasswordInput)
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'faraz@gmail.com'}))
    # image=forms.ImageField()
    # url=forms.URLField(initial="https//:", help_text='site address')
    # FAVORATE_FEILD=[
    #     ('0','select'),
    #      ('1','IT'),
    #      ('2','LOGESTIC'),
    #      ('3','ENGINEERING'),
    #      ('4','MARKETING')
  
    # ]
    
    # feild=forms.ChoiceField(choices=FAVORATE_FEILD)
    
    def clean_age(self):
        age1=self.cleaned_data['age']
        return age1
    
    def clean_name(self):
        name1=self.cleaned_data["name"]
        return name1
    
class Form2(forms.ModelForm):
    class Meta:
        model=Post
        fields="__all__"
        
        def clean_name(self):
            name1=self.cleaned_data['name']
            return name1
        def clean_family(self):
            family1=self.cleaned_data['family']
            return family1 
        
        def clean_age(self):
            age1=self.cleaned_data['age']
            return age1
            
        def clean_active(self):
            active=self.cleaned_data['is_active']
            return active