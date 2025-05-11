from django.contrib import admin
from myapp.models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'f_name', 'email', 'phone')
admin.site.register(User, UserAdmin)