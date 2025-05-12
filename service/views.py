from django.shortcuts import render
from service.models import Service
from . forms import User_Registeration

# Create your views here.
def service_app(request):
    service= Service.objects.all()
    if request.method == "POST":
        
        fm=User_Registeration(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data)
        else:
            print(fm.errors)
       
    else:
        fm=User_Registeration()
        print("not post")
    
    return render(request, 'service/service_app.html',{"service":service, "form":fm})
