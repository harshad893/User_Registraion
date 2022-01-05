from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from app.forms import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app.models import *

def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        return render(request,'home.html',{'username':username})
    return render(request,'home.html')


def registration(request):
    UF=UserForm()
    PF=ProfileForm()
    d={'UF':UF,'PF':PF}
    if request.method=='POST' and request.FILES:
        UD=UserForm(request.POST)
        PD=ProfileForm(request.POST,request.FILES)
        userobject=UD.save(commit=False)
        pw=UD.cleaned_data['password']
        userobject.set_password(pw)
        userobject.save()
        profileobject=PD.save(commit=False)
        profileobject.user=userobject
        profileobject.save()
        send_mail('Registration',
                    'Reg Is Done,Thanks',
                    'xxxxxxxxxxx@gmail.com',
                    [userobject.email],
                    fail_silently=False            
                                )
        return HttpResponse('Registration is done successfully')

    return render(request,'registration.html',d)

def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user and user.is_active:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))

    return render(request,'userlogin.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def profile_details(request):
    username=request.session.get('username')
    UD=User.objects.get(username=username)
    PD=Profile.objects.get(user=UD)
    d={'UD':UD,'PD':PD}
    return render(request,'profile_details.html',d)

@login_required
def change_password(request):
    if request.method=='POST':
        username=request.session.get('username')
        UD=User.objects.get(username=username)
        password=request.POST['password']
        UD.set_password(password)
        UD.save()
        return HttpResponse('password is changed successfully')
    return render(request,'change_password.html')
