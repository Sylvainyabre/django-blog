from django import template
from ..models import Article
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.simple_tag
def total_articles():
    return Article.objects.filter(status='published').count()


@register.inclusion_tag('my_site/latest_articles.html')
def show_latest_articles(count=5):
    latest_articles = Article.objects.filter(status='published').order_by('-pub_date')[:count]
    return {'latest_articles': latest_articles}


@register.simple_tag
def python_articles():
    return Article.objects.filter( status='published', content_category='python').order_by('-pub_date')


@register.simple_tag
def get_most_commented_articles(count=5):
    return Article.objects.filter(status='published').annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
