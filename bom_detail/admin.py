from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Bom_Detail

class BomDetailAdmin(admin.ModelAdmin):
    search_fields = ['rd','pn','bom__name','description','category1','category2','customer_pn']
    list_filter = ['bom__name','category1','category2','customer_pn']
    list_display = ('rd','pn','alt_pn','customer_pn','bom','description','category1','category2')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    fieldsets = [
        ('Basic Information',{'fields': ['rd','pn','slug','bom','alt_pn','description','category1','category2','user']}),
        ('Customer Information',{'fields': ['customer_pn']}),
    ]
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(BomDetailAdmin, self).save_model(request, obj, form, change)
admin.site.register(Bom_Detail,BomDetailAdmin)