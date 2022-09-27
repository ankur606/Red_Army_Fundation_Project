from atexit import register
from django.contrib import admin
from .models import PersonalInformation
# Register your models here.

@admin.register(PersonalInformation)

class PersonalInformationAdmin(admin.ModelAdmin):
    pass
