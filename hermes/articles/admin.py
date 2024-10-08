from django.contrib import admin
from .models import Post

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, ProjectAdmin)