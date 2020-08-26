from . import views as site_views
from django.urls import path
from .feeds import LatestArticlesFeed


urlpatterns = [
    path('', site_views.homepage, name='home'),
    path('article_detail/<slug>/<int:pk>/', site_views.article_detail, name='article_detail'),
    path('add_comment/<int:pk>/', site_views.add_comment, name='add_comment'),
    path('add_reply/<int:pk>/', site_views.add_reply, name='add_reply'),
    path('article/create/new/',site_views.create_article, name= 'create_article'),
    path('feed/', LatestArticlesFeed(), name='articles_feed'),
    path('search/',site_views.article_search, name='search'),
    path('about/me/', site_views.about, name = 'about'),
]
