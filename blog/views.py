from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse

from blog.BlogForm import BlogForm, BlogImageForm, CommentForm
from blog.models import BlogPost, BlogImage


def single_post(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    blog_image = BlogImage.objects.get(blogpost_id=blog_post.id)
    categories = blog_post.category.all()
    new_comment = None
    template = 'single_blog.html'

    if 'last_item' in request.session:
        del request.session['last_item']

    comment_form = CommentForm()

    context = {
        'blog_post': blog_post,
        'blog_image': blog_image,
        'comment_form': comment_form,
        'categories': categories
    }

    return render(request, template, context)


def all_blog(request):
    template = 'add_blog.html'
    return render(request, template)


def add_blog(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        blog_image_form = BlogImageForm(request.POST, request.FILES)
        if blog_form.is_valid() and blog_image_form.is_valid():
            new_blog = blog_form.save(commit=False)
            new_blog_image = blog_image_form.save(commit=False)
            new_blog.author = request.user
            new_blog.save()
            new_blog_image.blogpost_id_id = new_blog.pk
            new_blog_image.save()
            messages.success(request, 'Successfully posted your blog.')
        else:
            messages.error(request, 'Failed to add the blog. \
                           Please ensure the form is valid.')
    else:
        blog_form = BlogForm()
        blog_image_form = BlogImageForm()

    if 'last_item' in request.session:
        del request.session['last_item']

    context = {
        'blog_form': blog_form,
        'blog_image_form': blog_image_form,
    }

    template = 'add_blog.html'
    return render(request, template, context)


def edit_blog(request, blog_pk):
    blog_post = get_object_or_404(BlogPost, pk=blog_pk)
    blog_image = get_object_or_404(BlogImage, blogpost_id=blog_pk)

    if request.method == 'POST':
        blog_form = BlogForm(request.POST, instance=blog_post)
        blog_image_form = BlogImageForm(request.POST, request.FILES, instance=blog_image)

        if blog_form.is_valid() and blog_image_form.is_valid():
            updated_blog = blog_form.save(commit=False)
            updated_blog_image = blog_image_form.save(commit=False)
            updated_blog.author = request.user
            updated_blog.save()

            updated_blog_image.blogpost_id_id = updated_blog.pk
            updated_blog_image.save()
            messages.success(request, f'You updated {blog_post.title}!')

            if 'last_item' in request.session:
                del request.session['last_item']

            return redirect(reverse('single_post', args=[blog_post.slug]))
        else:
            messages.error(request, 'Failed to update blog. \
                                       Please ensure the form is valid.')
    else:
        blog_form = BlogForm(instance=blog_post)
        blog_image_form = BlogImageForm(request.POST, request.FILES, instance=blog_image)
        messages.info(
            request, f'You are editing a product details: {blog_post.title}')


        context = {
            'blog_form': blog_form,
            'blog_image_form': blog_image_form,
            'blog_post': blog_post,
        }
        template = 'edit_blog.html'

        return render(request, template, context)
