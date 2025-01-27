from django.contrib import admin

# Register your models here.
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('author', 'created_at')

admin.site.register(Note, NoteAdmin)
