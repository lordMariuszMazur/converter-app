from django.contrib import admin
from .models import Article, Comment


class CommnetInLine(admin.TabularInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommnetInLine,
    ]


admin.site.register(Article)
admin.site.register(Comment)
