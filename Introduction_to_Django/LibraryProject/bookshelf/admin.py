from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Columns to display in list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for easier navigation
    list_filter = ('author', 'publication_year')
    
    # Add a search bar for title and author
    search_fields = ('title', 'author')

# Register the Book model with the custom admin
admin.site.register(Book, BookAdmin)
