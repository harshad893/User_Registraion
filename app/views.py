from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from django.core.mail import send_mail
def home(request):
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