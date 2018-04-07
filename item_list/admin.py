from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import ItemList

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