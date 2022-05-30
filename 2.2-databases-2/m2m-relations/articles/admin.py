from django.contrib import admin
from .models import Article, ArticleScope, Tag
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        flag = False
        for form in self.forms:
            if form.cleaned_data.get('is_main') is True:
                if not flag:
                    flag = True
                else:
                    raise ValidationError('Основным может быть только один раздел')
        if not flag:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ArticleScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
