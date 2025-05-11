from django.shortcuts import render
from service.models import Service
from . forms import User_Registeration
# Create your views here.
def service_app(request):
    service= Service.objects.all()
    fm=User_Registeration()
    return render(request, 'service/service_app.html',{"service":service, "form":fm})