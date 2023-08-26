from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import ColorPalette, Color

# Register your models here.
class ColorInline(admin.TabularInline):
    model = Color
    extra = 1

@admin.register(ColorPalette)
class ColorPaletteAdmin(VersionAdmin):
    inlines = [ColorInline]
    list_display = ('name', 'owner', 'is_public')
    list_filter = ('is_public',)
    search_fields = ('name', 'owner__username')

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('value', 'role')
    list_filter = ('role',)
    search_fields = ('value',)

admin.site.site_header = 'Color Palette Admin'
