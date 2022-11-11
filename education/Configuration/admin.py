from django.contrib import admin

# Register your models here.
from .models import Staff,Student,Instructor



admin.site.register(Staff)
admin.site.register(Instructor)
admin.site.register(Student)