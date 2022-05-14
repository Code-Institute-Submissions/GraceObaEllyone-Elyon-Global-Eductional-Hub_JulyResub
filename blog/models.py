from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify

from course.models import Course, Category

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ManyToManyField(Category, null=True, blank=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return '{}, {}'.format(self.title, self.course)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)


class BlogImage(models.Model):
    image = models.ImageField(null=False)
    blogpost_id = models.ForeignKey('BlogPost', null=True, blank=True,
                                    on_delete=models.SET_NULL, verbose_name='image_blogpost_id')

    def __str__(self):
        return '{}, {}'.format(self.image, self.blogpost_id)


class BlogComment(models.Model):
    blogpost_id = models.ForeignKey('BlogPost', null=True, related_name='comments',
                                    blank=True, on_delete=models.SET_NULL)
    user_id = models.ForeignKey(User, null=True, blank=True,
                                on_delete=models.SET_NULL)
    comment_tittle = models.CharField(max_length=100)
    blog_comment = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='comment_created_date')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return '{}, {}, {}'.format(self.blogpost_id, self.user_id, self.comment_tittle)
