from django.contrib import admin
from testApp.models import hydjobs,bangjobs,chennaijobs,punejobs

# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','address','mail','mobile']


class BangjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','address','mail','mobile']

class ChennaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','address','mail','mobile']



class PunejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','address','mail','mobile']


admin.site.register(hydjobs,HydjobsAdmin)
admin.site.register(bangjobs,BangjobsAdmin)
admin.site.register(chennaijobs,ChennaijobsAdmin)
admin.site.register(punejobs,PunejobsAdmin)
