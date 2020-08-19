from django.contrib import admin
from .models import Article, Comment, CommentReply, About


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status')
    list_filter = ('status', 'created', 'author', 'pub_date')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'pub_date'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('author',)


class CommentReplyAdmin(admin.ModelAdmin):
    list_display = ( 'author', 'comment', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('author', 'body')


admin.site.register(About)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentReply, CommentReplyAdmin)

