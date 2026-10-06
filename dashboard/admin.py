from django.contrib import admin
from django.utils.html import format_html
from .models import GalleryImage

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("preview", "title", "category", "is_visible", "created")
    list_editable = ("category", "is_visible")
    list_filter = ("category", "is_visible")
    search_fields = ("title",)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;border-radius:6px">', obj.image.url)
        return ""