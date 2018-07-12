from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Bom

class BomAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2']
    list_filter = ['category1','category2','status']
    list_display = ('name','title','item_count','category1','category2','status','user')
    readonly_fields = ('user','slug')
    fieldsets = [
        ('Basic Information',{'fields': ['name','title','slug','description','category1','category2','status','user']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(BomAdmin, self).save_model(request, obj, form, change)

admin.site.register(Bom,BomAdmin)


from .models import Bom_Detail

class BomDetailAdmin(admin.ModelAdmin):
    search_fields = ['rd','pn','bom__name','description','category1','category2','customer_pn']
    list_filter = ['bom__name','category1','category2','customer_pn']
    list_display = ('rd','pn','pn_type','customer_pn','bom','description','category1','category2')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    fieldsets = [
        ('Basic Information',{'fields': ['rd','pn','pn_type','bom','description','category1','category2','user']}),
        ('Customer Information',{'fields': ['customer_pn']}),
    ]
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(BomDetailAdmin, self).save_model(request, obj, form, change)
admin.site.register(Bom_Detail,BomDetailAdmin)