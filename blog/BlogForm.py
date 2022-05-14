from django import forms

from blog.models import BlogPost, BlogImage, BlogComment


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ('slug', 'created_on', 'status', 'updated_on', 'author')


class BlogImageForm(forms.ModelForm):
    class Meta:
        model = BlogImage
        fields = ('image',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('comment_tittle', 'blog_comment')