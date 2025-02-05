from django.contrib import admin
from .models import Paper

@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'views')
    list_filter = ('publication',)
    search_fields = ('title', 'description')
