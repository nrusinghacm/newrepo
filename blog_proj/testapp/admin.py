from django.contrib import admin
from testapp.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('status','author','publish')#adding filter option in database
    search_fields=('title','body',)# adding search fields
    raw_id_fields=('author',)   # adding id instead of author name when blog added
    date_hierarchy='publish'    #adding date heararchy in admin
    ordering=['status','publish'] # showing how many data are present
    prepopulated_fields={'slug':('title',)}# adding slug field auto populated

admin.site.register(Post, PostAdmin)
