from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from parameter.models import Parameter,ParameterSet

class ParameterSetInline(admin.TabularInline):
    model = ParameterSet
    extra = 1 # how many rows to show
    # fields =('item','item__title')



class ParameterAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description']
    list_filter = []
    list_display = ('name','title','item_count','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    inlines=[ParameterSetInline]

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','description','slug','user']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ParameterAdmin, self).save_model(request, obj, form, change)

admin.site.register(Parameter,ParameterAdmin)