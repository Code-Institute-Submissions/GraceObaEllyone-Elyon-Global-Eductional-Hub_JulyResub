from django.shortcuts import render

# Create your views here.


def add_blog(request):

    template = 'add_blog.html'
    render(request, template)