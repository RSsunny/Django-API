from django.shortcuts import render

# Create your views here.
def service_app(request):
    return render(request, 'service/service_app.html')