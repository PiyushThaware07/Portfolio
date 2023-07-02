from django.shortcuts import render,HttpResponse,redirect
# Datetime
from django.utils import timezone
# DataBase
from . models import *


# Create your views here.
def index(request):
    education_details = Education.objects.all()
    experience_details = Experience.objects.all()
    return render(request,"Index.html",locals())

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        datetime = timezone.now()
        newContact = Contact(name=name,email=email,message=message,datetime=datetime)
        newContact.save()
        return redirect(f"/#contact")
