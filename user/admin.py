from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import WMPUser,UserAccess

# from django.contrib.auth.models import Permission
# admin.site.register(Permission)

# from shop.models import Employee

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class OperationInline(admin.StackedInline):
    model = UserAccess
    can_delete = True
    verbose_name_plural = 'Operation - Authentication'

from .forms import UserAdminChangeForm
# UserAdminCreationForm, 
# # Define a new User admin
class UserAdmin(BaseUserAdmin):
	form = UserAdminChangeForm
	list_display = ('username', 'first_name', 'last_name', 'department', 'is_staff')
	fieldsets = (
        ('General', {'fields': ('username', 'first_name', 
        	'last_name','password',
        	 'department', )}

        ),
        ('Permission',{'fields':('is_active', 'is_staff', 'is_superuser',
        	'groups', 'user_permissions')}),
      
    )
	inlines = [OperationInline]
	# filter_horizontal=['operations']
	class Meta:
		model = WMPUser
    # inlines = (EmployeeInline, )

# Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.unregister(User)
admin.site.register(WMPUser, UserAdmin)