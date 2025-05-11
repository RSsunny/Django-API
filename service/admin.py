from django.contrib import admin
from service.models import Service
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time', 'location', 'updated_at', 'price', 'is_active')

admin.site.register(Service, ServiceAdmin)