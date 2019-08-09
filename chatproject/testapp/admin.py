from django.contrib import admin
from .models import Chat1, Chat2

class ChatAdmin1(admin.ModelAdmin):
    list_display=["id","text"]
class ChatAdmin2(admin.ModelAdmin):
    list_display=["id","text"]

admin.site.register(Chat1, ChatAdmin1)
admin.site.register(Chat2, ChatAdmin2)
