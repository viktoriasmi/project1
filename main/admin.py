from django.contrib import admin

from main.models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')
    list_filter = ('publication_date',)
    search_fields = ('title', 'content')
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'content')
        }),
    )
