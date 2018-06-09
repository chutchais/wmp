from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from hook.models import Hook

    
class HookAdmin(admin.ModelAdmin):
    search_fields = ['name','description','title','event','category1','category2']
    list_filter = ['category1','category2','name','event','routing_detail']
    list_display = ('name','event','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    

    fieldsets = [
        ('Local Object',{'fields': ['name','title']}),
        ('Event Information',{'fields': ['ordered',('event','snippet'),'routing_detail']}),
         ('Basic Information',{'fields': ['description','slug','category1','category2','user']}),
    ]
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(HookAdmin, self).save_model(request, obj, form, change)

admin.site.register(Hook,HookAdmin)