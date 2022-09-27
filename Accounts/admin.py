from atexit import register
from django.contrib import admin

from Admin_dasboard.models import CommunityDiscussionsModel
from .models import *
from Admin_dasboard import*
# Register your models here.

@admin.register(CommunityDiscussionsModel)

class CommunityDiscussionsModelAdmin(admin.ModelAdmin):
    
    list_display=('topic_description','image')
    