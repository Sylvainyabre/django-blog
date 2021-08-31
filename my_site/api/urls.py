from django.urls import path
from . import views as api_views


app_name = "articles"
urlpatterns = [
    path('articles/', api_views.ArticleListView.as_view(),
         name='article_list'),
    path('articles/<pk>/', api_views.ArticleDetailView.as_view(),
         name='article_detail'),

]
