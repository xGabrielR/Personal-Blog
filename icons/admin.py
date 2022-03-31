from django.contrib import admin
from .models import Icon

@admin.register(Icon)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)
    list_display_links = ('id',)