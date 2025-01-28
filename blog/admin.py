from django.contrib import admin
from .models import Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','slug', 'status','publish' ]
    list_filter = ['title', 'author','publish', 'status']
    seach_fields = ['title', 'body']
    prepopulated_fields = {'slug':('title', )}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS
