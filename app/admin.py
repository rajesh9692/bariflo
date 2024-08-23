from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(signup)
class signup(admin.ModelAdmin):
    list_display =['first_name','last_name','email_id','phone_no','password']
