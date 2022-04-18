from django.contrib import admin

from books.book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass