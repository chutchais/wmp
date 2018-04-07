from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from routing_detail.models import RoutingDetail,RoutingDetailParameterSet

class RoutingDetailParameterInline(admin.TabularInline):
    model = RoutingDetailParameterSet
    extra = 1 # how many rows to show
    verbose_name = 'Parameter Configuration'
    verbose_name_plural = 'Parameter Configuration'
    
class RoutingDetailAdmin(admin.ModelAdmin):
    search_fields = ['operation','routing__name','description','category1','category2']
    list_filter = ['routing','category1','category2']
    list_display = ('operation','routing','position','next_pass','next_fail','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    # inlines=[RoutingAcceptSetInline,RoutingExceptSetInline,RoutingNextSetInline,RoutingDetailParameterInline]

    fieldsets = [
        ('Basic Information',{'fields': ['operation',('routing','position'),'description','slug','category1','category2','user']}),
        ('Next Operation Information (Default)',{'fields': ['next_pass','next_fail']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(RoutingDetailAdmin, self).save_model(request, obj, form, change)
admin.site.register(RoutingDetail,RoutingDetailAdmin)