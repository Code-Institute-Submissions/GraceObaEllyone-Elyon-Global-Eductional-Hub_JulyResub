from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify

# Create your models here.


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class BlogPost(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.CharField(max_length=300)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='post_created_name')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return '{}, {}'.format(self.title, self.category)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)


class BlogImage(models.Model):
    image = models.ImageField(null=False)
    blog_post_id = models.ForeignKey('BlogPost', null=True, blank=True,
                                     on_delete=models.SET_NULL, verbose_name='image_blog_post_id')

    def __str__(self):
        return '{}, {}'.format(self.image, self.blog_post_id)


class BlogComment(models.Model):
    blog_post_id = models.ForeignKey('BlogPost', null=True,
                                     related_name='comments', blank=True, on_delete=models.SET_NULL)
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    comment_title = models.CharField(max_length=100)
    comment_desc = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='comment_created_date')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return '{}, {}, {}'.format(self.blog_post_id, self.user_id, self.comment_title)