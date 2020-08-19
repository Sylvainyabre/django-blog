from django import forms
from .models import Comment, CommentReply, Article


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(label='Enter email address', widget=forms.PasswordInput)
    to = forms.EmailField()
    comment = forms.CharField(required=False)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = ('body',)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('author','slug','pub_date',)


class SearchForm(forms.Form):
    query = forms.CharField()



