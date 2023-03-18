from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from blog.models import Blog


class BlogInline(admin.StackedInline):
    model = Blog
    extra = 1


class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "is_superuser")
    list_filter = ("username",)
    inlines = [BlogInline]

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Permissions", {
         "fields": ("is_superuser", "is_staff", "user_permissions")
         }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2"),
        },
        ),
    )

    search_fields = ("username", "email")
    ordering = ("username", "email")

    filter_horizontal = ()


admin.site.register(User, UserAdmin)
