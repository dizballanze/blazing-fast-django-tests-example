from django.contrib import admin, messages

from blog.models import Article, Author


def clone_article(modeladmin, request, queryset):
    if queryset.count() != 1:
        modeladmin.message_user(request, "You could clone only one article at a time.", level=messages.ERROR)
        return
    origin_article = queryset.first()
    cloned_article = Article(
        title="{} (COPY)".format(origin_article.title),
        content=origin_article.content,
        created_at=origin_article.created_at,
        author_id=origin_article.author_id,
        comments_on=origin_article.comments_on)
    cloned_article.save()
    cloned_article.tags = origin_article.tags.all()
    modeladmin.message_user(request, "Article successfully cloned", level=messages.SUCCESS)
clone_article.short_description = 'Clone article'

class ArticleAdmin(admin.ModelAdmin):

    list_display = ['title']
    ordering = ['-created_at']
    actions = [clone_article]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
