from django.contrib import admin
from testapp.models import Gpsdata

class GpsdataAdmin(admin.ModelAdmin):
    list_display=['id','latitude']#,'longitude','speed','altitude','time']
    # list_filter=('speed','altitude','time')
    # search_fields=('time',)
admin.site.register(Gpsdata,GpsdataAdmin)
