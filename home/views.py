from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from about.models import About
from service.models import Service
from service.models import Service_type
from our_class.models import Class
from gallery.models import Gallery
from package.models import Package
from our_class.models import Class_Type
from training.models import Training
from time_table.models import Table
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
    ClassData=Class.objects.all()
    GalleryData=Gallery.objects.all()
    PackageData=Package.objects.all()
    ClassTypeData=Class_Type.objects.all()
    TrainingData=Training.objects.all()
    TableData=Table.objects.all()
    data={
        'AboutData':AboutData,
        'ServiceData':ServiceData,
        'ServiceType':ServiceType,
        'ClassData':ClassData,
        'GalleryData':GalleryData,
        'PackageData':PackageData,
        'ClassTypeData':ClassTypeData,
        'TrainingData':TrainingData,
        'TableData':TableData,
    }    
    return render(request,'index.html',data)
def message(request):
    return render(request,'message.html')