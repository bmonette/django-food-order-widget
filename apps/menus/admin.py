from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "restaurant", "sort_order", "is_active")
    list_filter = ("is_active", "restaurant")
    search_fields = ("name",)
    ordering = ("restaurant", "sort_order", "name")
