from django.contrib import admin
from .models import Questions, Questionpaper, Student

# Register your models here.
admin.site.register(Questions)
admin.site.register(Questionpaper)
admin.site.register(Student)