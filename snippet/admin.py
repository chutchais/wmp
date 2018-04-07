from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Snippet

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