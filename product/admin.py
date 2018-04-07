from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','pn','customer_pn']
    list_filter = ['pn','category1','category2','customer_pn']
    list_display = ('name','title','pn','rev','customer_pn','customer_rev','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    fieldsets = [
        ('Basic Information',{'fields': ['name','title','slug','pn','rev','description','category1','category2','user']}),
        ('Work Order Control',{'fields': ['regexp']}),
        ('Customer Information',{'fields': ['customer_pn','customer_rev']}),
        ('Routing Control',{'fields': ['routing']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ProductAdmin, self).save_model(request, obj, form, change)
admin.site.register(Product,ProductAdmin)