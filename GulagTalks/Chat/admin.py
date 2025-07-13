from django.contrib import admin
from .models import GC_messages, GroupChats

# Register your models here.
admin.site.register(GroupChats)
admin.site.register(GC_messages)