from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Item
from .models import ItemList
# class ItemListline(admin.):
class ItemListline(admin.TabularInline):
    model = ItemList
    extra = 0
    can_delete = True
    verbose_name_plural = 'Item list configuration'



class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','product__name','category1','category2']
    list_filter = ['input_type','product','category1','category2']
    list_display = ('name','title','input_type','has_validation_code','description','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug','has_validation_code')
    inlines=[ItemListline]


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


class ItemListAdmin(admin.ModelAdmin):
    search_fields = ['name','title','value','item__name']
    list_filter = []
    list_display = ('name','title','value','item','ordered')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','item','slug','user']}),
        ('Value',{'fields': ['value','default']}),
        ('Ordering',{'fields': ['ordered']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ItemListAdmin, self).save_model(request, obj, form, change)

admin.site.register(ItemList,ItemListAdmin)