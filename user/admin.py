from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import WMPUser

# from shop.models import Employee

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
# class EmployeeInline(admin.StackedInline):
#     model = Employee
#     can_delete = False
#     verbose_name_plural = 'employee'

from .forms import UserAdminChangeForm
# UserAdminCreationForm, 
# # Define a new User admin
class UserAdmin(BaseUserAdmin):
	form = UserAdminChangeForm
	list_display = ('username', 'first_name', 'last_name', 'department', 'is_staff')
	fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name', 'department', 'is_staff')}),
      
    )
	class Meta:
		model = WMPUser
    # inlines = (EmployeeInline, )

# Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.unregister(User)
admin.site.register(WMPUser, UserAdmin)