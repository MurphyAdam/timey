from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_filter = ('id', 'date_joined', 'email_verified')
    search_fields = ('username', )
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            # group heading of your choice; set to None for a blank space instead of a header
            'Email verified',
            {
                'fields': (
                    'email_verified',
                ),
            },
        ),
        (
            'User type',
            {
                'fields': (
                    'user_type',
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
