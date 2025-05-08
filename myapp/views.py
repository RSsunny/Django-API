from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myApp(request):
    return HttpResponse("" \
        "<h1>Welcome to myApp</h1>" \
        "<p>This is a simple Django application.</p>" \
        "<p>Explore the API and enjoy!</p>"
        "<p>Click <a href='/admin/'>here</a> to go to the admin page.</p>"
        "<p>Click <a href='/myapp/'>here</a> to go to the myapp page.</p>"
        "<p>Click <a href='/myapp/hello/'>here</a> to go to the hello page.</p>"
        "<p>Click <a href='/myapp/goodbye/'>here</a> to go to the goodbye page.</p>"
        "<p>Click <a href='/myapp/hello/John/'>here</a> to go to the hello John page.</p>"
        "<p>Click <a href='/myapp/goodbye/John/'>here</a> to go to the goodbye John page.</p>"
        "<p>Click <a href='/myapp/hello/John/age/30/'>here</a> to go to the hello John age page.</p>"
        "<p>Click <a href='/myapp/goodbye/John/age/30/'>here</a> to go to the goodbye John age page.</p>"
        "<p>Click <a href='/myapp/hello/John/age/30/country/USA/'>here</a> to go to the hello John age country page.</p>"
        "<p>Click <a href='/myapp/goodbye/John/age/30/country/USA/'>here</a> to go to the goodbye John age country page.</p>"
        "<p>Click <a href='/myapp/hello/John/age/30/country/USA/city/NewYork/'>here</a> to go to the hello John age country city page.</p>"
        "<p>Click <a href='/myapp/goodbye/John/age/30/country/USA/city/NewYork/'>here</a> to go to the goodbye John age country city page.</p>"
        "<p>Click <a href='/myapp/hello/John/age/30/country/USA/city/NewYork/language/English/'>here</a> to go to the hello John age country city language page.</p>"
    )