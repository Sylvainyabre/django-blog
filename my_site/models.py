from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings


class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'), )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blog_posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    illustration = models.ImageField(blank=True, null=True, default='article.png', upload_to='media/')
    description = models.TextField(blank=True,null=True)
    content_category = models.CharField(max_length=25, choices=[('python', 'python'),
                                                                ('javaScript', 'javaScript'),
                                                                ('html', 'html'),
                                                                ('css', 'css'),], default='Unclassified')
    content = RichTextUploadingField()
    status = models.CharField(max_length=100,
                              choices=STATUS_CHOICES,
                              default='draft')
    slug = models.SlugField(max_length=50,
                            unique_for_date='pub_date')

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug, 'pk': self.pk})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    body = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'comment by{} on {}'.format(self.author, self.article)


class CommentReply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    body =  RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
        verbose_name_plural = 'CommentReplies'

    def __str__(self):
        return '{} on {}'.format(self.author, self.created)


class About(models.Model):
    about = RichTextUploadingField()

    def __str__(self):
        return 'about Programming Literacy'

    def get_absolute_url(self):
        return reverse('about', kwargs={'pk': self.pk})



