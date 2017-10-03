from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
# Register your models here.
from .models import (Bom,
					 BomDetail,
                     Item,ItemList,
					 Operation,
                     Parameter,ParameterSet,
					 Performing,
					 Product,
					 Routing,
					 RoutingDetail,
					 SerialNumber,
                     Snippet,
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
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(BomDetailAdmin, self).save_model(request, obj, form, change)
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

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(OperationAdmin, self).save_model(request, obj, form, change)

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
        ('Work Order Control',{'fields': ['regexp']}),
        ('Customer Information',{'fields': ['customer_pn','customer_rev']}),
        ('Routing Control',{'fields': ['routing']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ProductAdmin, self).save_model(request, obj, form, change)
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

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(RoutingAdmin, self).save_model(request, obj, form, change)
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

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(RoutingDetailAdmin, self).save_model(request, obj, form, change)
admin.site.register(RoutingDetail,RoutingDetailAdmin)

class WorkOrderAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','product__name','category1','category2']
    list_filter = ['product','category1','category2']
    list_display = ('name','title','product','qty','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    fieldsets = [
        ('Basic Information',{'fields': ['name','title','product','qty','description','slug','category1','category2','user']}),
        ('Serial Number Control',{'fields': ['regexp']}),
        ('Routing Control',{'fields': ['routing']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(WorkOrderAdmin, self).save_model(request, obj, form, change)
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

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(SerialNumberAdmin, self).save_model(request, obj, form, change)
admin.site.register(SerialNumber,SerialNumberAdmin)


class ItemListAdmin(admin.ModelAdmin):
    search_fields = ['name','title','value','parameter__name']
    list_filter = []
    list_display = ('name','title','value','parameter','ordered')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','parameter','slug','user']}),
        ('Value',{'fields': ['value','default']}),
        ('Ordering',{'fields': ['ordered']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ItemListAdmin, self).save_model(request, obj, form, change)

admin.site.register(ItemList,ItemListAdmin)

class ItemListline(admin.TabularInline):
    model = ItemList
    extra = 1

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ItemListline, self).save_model(request, obj, form, change)

class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description','product__name','category1','category2']
    list_filter = ['input_type','product','category1','category2']
    list_display = ('name','title','input_type','product','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    inlines=[ItemListline]

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','product','description','slug','category1','category2','user']}),
        ('Input Type',{'fields': ['input_type','help_text']}),
        ('Text Box Information',{'fields': ['default_value','regexp']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ItemAdmin, self).save_model(request, obj, form, change)

admin.site.register(Item,ItemAdmin)


class ParameterSetInline(admin.TabularInline):
    model = ParameterSet
    extra = 1 # how many rows to show

class ParameterAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description']
    list_filter = []
    list_display = ('name','title','item_count','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    inlines=[ParameterSetInline]

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','slug','user']}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ParameterAdmin, self).save_model(request, obj, form, change)

admin.site.register(Parameter,ParameterAdmin)

class SnippetAdmin(admin.ModelAdmin):
    search_fields = ['name','title','description']
    list_filter = ['category1','category2']
    list_display = ('name','title','description','category1','category2','created_date')
    # list_editable = ('color','move_performa')
    readonly_fields = ('user','slug')
    # formfield_overrides = {
    #     # models.CharField: {'widget': TextInput(attrs={'size':'20'})},
    #     models.TextField: {'widget': Textarea(attrs={'rows':20, 'cols':40})},
    # }

    fieldsets = [
        ('Basic Information',{'fields': ['name','title','description','slug','user']}),
        ('Category',{'fields': [('category1','category2')]}),
        ('Code',{'fields': ['code']}),
    ]
    def get_form(self, request, obj=None, **kwargs):
        form = super(SnippetAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['code'].widget.attrs['style'] = 'width:800px; height:500px;'
        return form

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(SnippetAdmin, self).save_model(request, obj, form, change)

admin.site.register(Snippet,SnippetAdmin)