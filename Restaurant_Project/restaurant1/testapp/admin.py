from django.contrib import admin
from .models import Restaurant
# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display=['res_id','address','locality','city']
    list_filter=('city','locality')
    search_fields=('city',)


admin.site.register(Restaurant, RestaurantAdmin)
