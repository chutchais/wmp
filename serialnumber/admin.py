from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import SerialNumber

class SerialNumberAdmin(admin.ModelAdmin):
    search_fields = ['number','workorder','description']
    list_filter = ['current_operation','wip']
    list_display = ('number','workorder','current_operation','wip')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug','parent','unit_type')
    fieldsets = [
        ('Basic Information',{'fields': ['number','workorder','unit_type','description','category1','category2','wip','user']}),
        ('Assembly Imformation',{'fields': ['parent']}),
        ('Performing',{'fields': ['current_operation',('perform_operation','perform_start_date')]}),
        ('Last Performance',{'classes': ('collapse','wide', 'extrapretty'),'fields': ['last_operation','last_result','routing']}),
        ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(SerialNumberAdmin, self).save_model(request, obj, form, change)
admin.site.register(SerialNumber,SerialNumberAdmin)