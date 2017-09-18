from django.contrib import admin

# Register your models here.
from .models import (Bom,
					 BomDetail,
					 Operation,
					 Performing,
					 Product,
					 Routing,
					 RoutingDetail,
					 SerialNumber,
					 WorkOrder,
					 )

class BomAdmin(admin.ModelAdmin):
    search_fields = ['name','description','category1','category2']
    list_filter = ['category1','category2','status']
    list_display = ('name','description','item_count','category1','category2','status','user')
    # list_editable = ('color','move_performa')
    fieldsets = [
        ('Basic Information',{'fields': ['name','description','category1','category2','status','user']}),
    ]
admin.site.register(Bom,BomAdmin)

class BomDetailAdmin(admin.ModelAdmin):
    search_fields = ['rd','pn','bom__name','description','category1','category2','customer_pn']
    list_filter = ['bom__name','category1','category2','customer_pn']
    list_display = ('rd','pn','alt_pn','customer_pn','description','category1','category2')
    # list_editable = ('color','move_performa')
    fieldsets = [
        ('Basic Information',{'fields': ['rd','pn','bom','alt_pn','description','category1','category2','user']}),
        ('Customer Information',{'fields': ['customer_pn']}),
    ]
admin.site.register(BomDetail,BomDetailAdmin)



class OperationAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2','customer_name']
    list_filter = ['category1','category2','customer_name']
    list_display = ('name','customer_name','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    fieldsets = [
        ('Basic Information',{'fields': ['name','title','description','category1','category2','user']}),
        ('Customer Information',{'fields': ['customer_name']}),
    ]
admin.site.register(Operation,OperationAdmin)

admin.site.register(Performing)

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2','customer_pn','routing']
    list_filter = ['pn','category1','category2','customer_pn']
    list_display = ('name','title','pn','rev','customer_pn','customer_rev','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    fieldsets = [
        ('Basic Information',{'fields': ['name','title','pn','rev','description','category1','category2']}),
        ('Customer Information',{'fields': ['customer_pn','customer_rev']}),
        ('Routing Control',{'fields': ['routing']}),
    ]
admin.site.register(Product,ProductAdmin)


class RoutingAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2']
    list_filter = ['category1','category2']
    list_display = ('name','title','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    fieldsets = [
        ('Basic Information',{'fields': ['name','title','description','category1','category2']}),
    ]
admin.site.register(Routing,RoutingAdmin)


class RoutingDetailAdmin(admin.ModelAdmin):
    search_fields = ['operation','routing__name','description','category1','category2']
    list_filter = ['category1','category2']
    list_display = ('operation','routing','position','next_pass','next_fail','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    fieldsets = [
        ('Basic Information',{'fields': ['operation','routing','description','category1','category2']}),
        ('Next Operation Information',{'fields': ['position','next_pass','next_fail']}),
    ]
admin.site.register(RoutingDetail,RoutingDetailAdmin)


class WorkOrderAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','product','category1','category2']
    list_filter = ['product','category1','category2']
    list_display = ('name','title','product','qty','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    fieldsets = [
        ('Basic Information',{'fields': ['name','title','product','qty','description','category1','category2']}),
        ('Routing Control',{'fields': ['routing']}),
    ]
admin.site.register(WorkOrder,WorkOrderAdmin)


class SerialNumberAdmin(admin.ModelAdmin):
    search_fields = ['number','workorder','description']
    list_filter = ['current_operation','wip']
    list_display = ('number','workorder','current_operation','wip')
    # list_editable = ('color','move_performa')
    fieldsets = [
        ('Basic Information',{'fields': ['number','workorder','description','category1','category2']}),
        ('Routing Control',{'fields': ['wip','current_operation','last_operation','last_modified_date']}),
        ('Performing',{'fields': ['perform_operation','perform_start_date']}),
    ]
admin.site.register(SerialNumber,SerialNumberAdmin)


