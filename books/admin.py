from django.contrib import admin
from books.models import Author, Book
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('AuthorID', 'Name', 'Age', 'Country')
    search_fields = ('Name',)
class BookAdmin(admin.ModelAdmin):
    list_display = ('ISBN', 'AuthorID', 'Title', 'Publisher', 'PublishDate', 'Price')
    ordering = ('ISBN',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
