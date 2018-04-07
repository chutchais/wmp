
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from routing_reject.models import RoutingReject

class RoutingRejectAdmin(admin.ModelAdmin):
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
        super(RoutingRejectAdmin, self).save_model(request, obj, form, change)
admin.site.register(RoutingReject,RoutingRejectAdmin)