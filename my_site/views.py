from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.text import slugify
from .forms import SearchForm
from .models import Article, Comment, About
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm, CommentReplyForm, ArticleForm
from django.contrib.postgres.search import SearchVector, SearchQuery,SearchRank


def homepage(request):
    template_name = 'my_site/home.html'
    articles = Article.objects.filter(status='published')
    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 6)  # show 5 articles at once on a page

    page_number = request.GET.get(page)
    page_object = paginator.get_page(page_number)

    context = {'articles': articles, 'page_object':page_object}
    return render(request,template_name , context=context)


def about(request):
    template_name = 'my_site/about.html'
    about_page = get_object_or_404(About, pk=1 )
    context = {'about_page':about_page}
    return render(request, template_name, context=context )


@staff_member_required
def create_article(request):
    template_name = 'my_site/article_creation.html'
    new_article = None
    if request.method == 'POST':
        article_form = ArticleForm(data=request.POST)
        if article_form.is_valid():
            new_article = article_form.save(commit=False)

            new_article.author = request.user
            if not new_article.slug:
                new_article.slug = slugify(new_article.title)

            messages.success(request, ' {}, your post [{}] has been submitted;'
                                      'it will be reviewed by admin for final approval.'
                                      ' Thank you for your contribution.'.format(new_article.author,
                                                                                 new_article.title))
            new_article.save()
            return redirect(reverse('home'))
    else:
        article_form = ArticleForm()
    return render(request, template_name, {'article_form': article_form, 'new_article': new_article})


@login_required
def article_detail(request, slug, pk):
    template_name = 'my_site/article_detail.html'
    article = get_object_or_404(Article, status='published', slug=slug, pk=pk)
    return render(request, template_name,
                  {'article': article})


def add_comment(request, pk):
    template_name = 'my_site/comment.html'
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # if the form is valid, create a comment form but don't save yet
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.author = request.user
            # assign the current article to the comment
            new_comment.save()
            # now save it to the database
            return redirect(reverse('home'))

    else:
        comment_form = CommentForm()
    return render(request, template_name,
                  {'new_comment': new_comment,
                   'comments': comments,
                   'comment_form': comment_form})


def add_reply(request, pk):
    template_name = 'my_site/reply_to_comments.html'
    comment = get_object_or_404(Comment, pk=pk)
    article = comment.article
    replies = comment.replies.filter(active=True)

    new_reply = None

    if request.method == 'POST':
        reply_form = CommentReplyForm(data=request.POST)
        if reply_form.is_valid():
            new_reply = reply_form.save(commit=False)
            new_reply.comment = comment
            new_reply.author = request.user
            new_reply.save()
            return redirect(reverse('home'))
    else:
        reply_form = CommentReplyForm()

    return render(request, template_name, {'new_reply': new_reply,
                                           'comment': comment,
                                           'article': article,
                                           'replies': replies,
                                           'reply_form': reply_form,
                                           })


def article_search(request):
    template_name = 'my_site/search.html'
    search_form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            search_vector = SearchVector('title', 'content')
            search_query = SearchQuery(query)
            results = Article.objects.annotate(
                search=search_vector,
                rank = SearchRank(search_vector, search_query)
            ).filter(search=search_query).order_by('-rank')
    context = {'search_form': search_form, 'results': results, 'query': query}

    return render(request, template_name, context)


