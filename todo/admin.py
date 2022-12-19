from django.contrib import admin
from .models import Note

class NotesAdmin(admin.ModelAdmin):
    readonly_fields = ('createdAt', )

# Register your models here.
admin.site.register(Note, NotesAdmin)