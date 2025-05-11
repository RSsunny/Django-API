from django.shortcuts import render
# Create your views here.
from myapp.models import User
def myApp(request):
    user= User.objects.all()
    return render(request, 'home/home.html', {"user": user})
    

