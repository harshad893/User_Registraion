from django.shortcuts import render

# Create your views here.
from app.forms import *

def home(request):
    return render(request,'home.html')


def registration(request):
    UF=UserForm()
    PF=ProfileForm()
    d={'UF':UF,'PF':PF}
    return render(request,'registration.html',d)