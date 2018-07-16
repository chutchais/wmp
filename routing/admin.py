from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Routing

class RoutingAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2']
    list_filter = ['category1','category2']
    list_display = ('name','title','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    fieldsets = [
        ('Basic Information',{'fields': ['name','title','description','slug','category1','category2','user']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(RoutingAdmin, self).save_model(request, obj, form, change)
admin.site.register(Routing,RoutingAdmin)




from routing.models import (RoutingDetail,RoutingDetailParameterSet,
                                    RoutingDetailAcceptSet,RoutingDetailRejectSet,RoutingDetailNextSet)
from routing_accept.models import RoutingAccept
from routing_reject.models import RoutingReject
from hook.models import Hook


class NextOperationInline(admin.TabularInline):
    model = RoutingDetailNextSet
    extra = 0 # how many rows to show
    verbose_name = 'Next Operation Condition'
    verbose_name_plural = 'Next Operation Condition'

class HookInline(admin.TabularInline):
    model = Hook
    extra = 0 # how many rows to show
    verbose_name = 'Hook - Local event Configuration'
    verbose_name_plural = 'Hook - Local event Configuration'

class RoutingDetailParameterInline(admin.TabularInline):
    model = RoutingDetailParameterSet
    extra = 0 # how many rows to show
    verbose_name = 'Parameter Configuration'
    verbose_name_plural = 'Parameter Configuration'

class AcceptInline(admin.TabularInline):
    model = RoutingDetailAcceptSet
    extra = 0
    can_delete = True
    verbose_name_plural = 'Routing - Accept'

class RejectInline(admin.TabularInline):
    model = RoutingDetailRejectSet
    extra = 0
    can_delete = True
    verbose_name_plural = 'Routing - Reject'
    
class RoutingDetailAdmin(admin.ModelAdmin):
    search_fields = ['operation','routing__name','description','category1','category2']
    list_filter = ['routing','category1','category2']
    list_display = ('operation','routing','position','next_pass','next_fail','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    

    fieldsets = [
        ('Basic Information',{'fields': ['operation',('routing','position'),'description','slug','category1','category2','user']}),
        ('Next Operation Information (Default)',{'fields': ['next_pass','next_fail']}),
    ]
    inlines = [AcceptInline,RejectInline,RoutingDetailParameterInline,NextOperationInline,HookInline]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(RoutingDetailAdmin, self).save_model(request, obj, form, change)
admin.site.register(RoutingDetail,RoutingDetailAdmin)


from routing.models import RoutingDetailNext

class RoutingDetailNextAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2']
    list_filter = ['category1','category2']
    list_display = ('name','title','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','description','slug','category1','category2','user']}),
        ('Except Code',{'fields': ['snippet']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(RoutingDetailNextAdmin, self).save_model(request, obj, form, change)
admin.site.register(RoutingDetailNext,RoutingDetailNextAdmin)