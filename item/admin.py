from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Item

class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','product__name','category1','category2']
    list_filter = ['input_type','product','category1','category2']
    list_display = ('name','title','input_type','has_validation_code','description','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug','has_validation_code')
    # inlines=[ItemListline]


    fieldsets = [
        ('Basic Information',{'fields': ['name','title','product','description','has_validation_code','slug','category1','category2','user']}),
        ('Input Type',{'fields': ['input_type','help_text']}),
        ('Text Box Information',{'fields': ['default_value','regexp']}),
        ('Validation Code',{'fields': ['snippet','expected_return']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ItemAdmin, self).save_model(request, obj, form, change)

admin.site.register(Item,ItemAdmin)