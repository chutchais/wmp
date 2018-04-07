from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import WorkOrder


class WorkOrderAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','product__name','category1','category2']
    list_filter = ['product','category1','category2']
    list_display = ('name','title','product','routing','qty','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    fieldsets = [
        ('Basic Information',{'fields': ['name','title','product','qty','description','slug','category1','category2','user']}),
        ('Serial Number Control',{'fields': ['regexp']}),
        ('Routing Control',{'fields': ['routing']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(WorkOrderAdmin, self).save_model(request, obj, form, change)
admin.site.register(WorkOrder,WorkOrderAdmin)