from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Article


class LatestArticlesFeed(Feed):
    title = 'Youth Garden'
    link = '/'
    description = 'New articles posted on my blog'

    def items(self):
        return Article.objects.filter(status='published')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)
