__author__ = 'jxl'
from django.contrib import admin
from ltblog.models import Category, Entry, Document

from ltblog.models import Category, Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title','author','category','pub_date')
    search_fields = ('title','category')

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('docfile', 'upload_date')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Entry, EntryAdmin)