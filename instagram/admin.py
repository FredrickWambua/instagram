from django.contrib import admin
from .models import Profile, User, Post, Comment


# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'commented_on',)
    list_filter = ('active', 'commented_on')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


