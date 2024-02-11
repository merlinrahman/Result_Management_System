from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import MyUser, Profile
# Register your models here.

class MyUserAdmin(BaseUserAdmin):
    list_display=('email','full_name','date_joined', 'last_login', 'is_admin','is_active')
    search_fields=('email','full_name')
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()

    add_fieldsets=(
        (None, {
            'classes':('wide'),
            'fields':('email','full_name','password1','password2'),
        }),
    )

    ordering=('email',)

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Profile)