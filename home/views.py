from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from about.models import About
from service.models import Service
from service.models import Service_type
# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        message=request.POST.get('message')
        if name and email and mobile and message:
            contact = Contact(name=name, email=email, mobile=mobile, message=message)
            contact.save()
            return redirect('message')
    AboutData=About.objects.all()
    ServiceData=Service.objects.all()
    ServiceType=Service_type.objects.all()
    data={
        'AboutData':AboutData,
        'ServiceData':ServiceData,
        'ServiceType':ServiceType,
    }    
    return render(request,'index.html',data)
def message(request):
    return render(request,'message.html')