from django.shortcuts import render,HttpResponse,redirect
# Datetime
from django.utils import timezone
# DataBase
from . models import *


# Create your views here.
def index(request):
    education_details = Education.objects.all()
    experience_details = Experience.objects.all()
    project_details = Project.objects.all()

    # Portfolio
    portfolio_instance = Portfolio.objects.first()
    firstName = portfolio_instance.firstName
    lastName = portfolio_instance.lastName
    fullName = portfolio_instance.fullName
    description =portfolio_instance.description
    short_desc = portfolio_instance.short_desc
    # Social Media
    facebook_url = portfolio_instance.facebook_url
    instagram_url = portfolio_instance.instagram_url
    snapchat_url = portfolio_instance.snapchat_url
    github_url = portfolio_instance.github_url
    linkedin_url = portfolio_instance.linkedin_url
    email_url = portfolio_instance.email_url
    # CV
    cv_url = portfolio_instance.cv_url
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
