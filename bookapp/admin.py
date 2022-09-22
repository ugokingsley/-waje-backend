from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class BookAdmin(ImportExportModelAdmin):
	list_display = ('name','isbn','author')
	list_filter = ('name',)
	search_fields = ['name']
admin.site.register(Book, BookAdmin)

class AuthorAdmin(ImportExportModelAdmin):
	list_display = ('first_name','last_name')
	list_filter = ('first_name',)
	search_fields = ['first_name']
admin.site.register(Author, AuthorAdmin)

