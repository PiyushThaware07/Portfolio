from django.shortcuts import render,HttpResponse

# DataBase
from . models import *


# Create your views here.
def index(request):
    education_details = Education.objects.all()
    return render(request,"Index.html",locals())
