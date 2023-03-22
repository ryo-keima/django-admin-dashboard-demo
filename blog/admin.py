from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = ("author",)
    search_fields = ("title",)
    ordering = ("title", )
    raw_id_fields = ('author',)


admin.site.register(Blog, BlogAdmin)
