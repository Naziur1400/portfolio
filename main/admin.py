from django.contrib import admin
from .models import Project, Contact, Info

# Register your models here.

admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(Info)