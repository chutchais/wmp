from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Operation

class OperationAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2','customer_name']
    list_filter = ['category1','category2','customer_name']
    list_display = ('name','customer_name','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    fieldsets = [
        ('Basic Information',{'fields': ['name','title','slug','description','category1','category2','user']}),
        ('Operation Type',{'fields': ['operation_type']}),
        ('Customer Information',{'fields': ['customer_name']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(OperationAdmin, self).save_model(request, obj, form, change)

admin.site.register(Operation,OperationAdmin)
