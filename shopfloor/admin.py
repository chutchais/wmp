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
    search_fields = ['name','title','description','category1','category2']
    list_filter = ['category1','category2','status']
    list_display = ('name','title','item_count','category1','category2','status','user')
    # date_hierarchy = 'created_date'
    # list_editable = ('color','move_performa')
    # list_display_links = ('name', 'title')
    # prepopulated_fields = {"title": ("title",)}
    readonly_fields = ('user','slug')
    fieldsets = [
        ('Basic Information',{'fields': ['name','title','slug','description','category1','category2','status','user']}),
    ]
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(BomAdmin, self).save_model(request, obj, form, change)

admin.site.register(Bom,BomAdmin)

class BomDetailAdmin(admin.ModelAdmin):
    search_fields = ['rd','pn','bom__name','description','category1','category2','customer_pn']
    list_filter = ['bom__name','category1','category2','customer_pn']
    list_display = ('rd','pn','alt_pn','customer_pn','bom','description','category1','category2')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
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
    readonly_fields = ('user','slug')
    fieldsets = [
        ('Basic Information',{'fields': ['name','title','slug','description','category1','category2','user']}),
        ('Customer Information',{'fields': ['customer_name']}),
    ]
admin.site.register(Operation,OperationAdmin)

admin.site.register(Performing)

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','pn','customer_pn']
    list_filter = ['pn','category1','category2','customer_pn']
    list_display = ('name','title','pn','rev','customer_pn','customer_rev','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    fieldsets = [
        ('Basic Information',{'fields': ['name','title','slug','pn','rev','description','category1','category2','user']}),
        ('Customer Information',{'fields': ['customer_pn','customer_rev']}),
        ('Routing Control',{'fields': ['routing']}),
    ]
admin.site.register(Product,ProductAdmin)


class RoutingAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','category1','category2']
    list_filter = ['category1','category2']
    list_display = ('name','title','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    fieldsets = [
        ('Basic Information',{'fields': ['name','title','description','slug','category1','category2','user']}),
    ]
admin.site.register(Routing,RoutingAdmin)


class RoutingDetailAdmin(admin.ModelAdmin):
    search_fields = ['operation','routing__name','description','category1','category2']
    list_filter = ['category1','category2']
    list_display = ('operation','routing','position','next_pass','next_fail','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    fieldsets = [
        ('Basic Information',{'fields': ['operation','routing','description','slug','category1','category2','user']}),
        ('Next Operation Information',{'fields': ['position','next_pass','next_fail']}),
    ]
admin.site.register(RoutingDetail,RoutingDetailAdmin)


class WorkOrderAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','product__name','category1','category2']
    list_filter = ['product','category1','category2']
    list_display = ('name','title','product','qty','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    fieldsets = [
        ('Basic Information',{'fields': ['name','title','product','qty','description','slug','category1','category2','user']}),
        ('Routing Control',{'fields': ['routing']}),
    ]
admin.site.register(WorkOrder,WorkOrderAdmin)


class SerialNumberAdmin(admin.ModelAdmin):
    search_fields = ['number','workorder','description']
    list_filter = ['current_operation','wip']
    list_display = ('number','workorder','current_operation','wip')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    fieldsets = [
        ('Basic Information',{'fields': ['number','workorder','description','slug','category1','category2','wip','user']}),
        ('Performing',{'fields': ['current_operation',('perform_operation','perform_start_date')]}),
        ('Last Performance',{'classes': ('collapse','wide', 'extrapretty'),'fields': ['last_operation','last_result','last_modified_date','routing']}),
        ]
admin.site.register(SerialNumber,SerialNumberAdmin)