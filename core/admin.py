from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.forms import UserProfileCreationForm, UserProfileUpdateForm
from core.models import CustomUser

class CustomUserAdmin(UserAdmin):
    '''
    Extending the "UserAdmin model" with the "custom form_field(s)" and the "CustomUser model"
    '''
    
    add_form = UserProfileCreationForm
    form = UserProfileUpdateForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email',  'is_staff',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'phone', 'city', 'state', 'country',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', 'phone', 'city', 'state', 'country',)}),
    )

# Registering the "CustomUser model" and the "CustomUserAdmin" model
admin.site.register(CustomUser, CustomUserAdmin)