from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from.forms import UserForm

def home(request):
    form=UserForm()
    return render(request,'home.html',{'form2':form})
    
def user(request):
    if request.method=='POST':
        fm=UserForm(request.POST)
        if fm.is_valid():
            First_name=fm.cleaned_data['First_name']
            Last_name=fm.cleaned_data['Last_name']
            designation=fm.cleaned_data['designation']
            email=fm.cleaned_data['email']
            contact=fm.cleaned_data['contact']
          
           
            User.first_name=First_name
            User.last_name=Last_name
            User.designation=designation
            User.email=email
            User.contact=contact
            User.save()
            return redirect('/home.html/')
    else:        
        return "exception"