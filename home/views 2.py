from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render


# Create your views here.
from course.models import Course, Category


def index(request):
    course_list = Course.objects.all()
    total = course_list.count()

    paginator = Paginator(course_list, 6)
    page = request.GET.get('page')

    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    categoryList = Category.objects.all()
    categoryTotal = categoryList.count()

    context = {
        'courses': courses,
        'total': total,
        'categories': categoryList,
        'categoryTotal': categoryTotal
    }

    template = 'index.html'
    return render(request, template, context)


def contactform(request):
    template = 'contact.html'
    return render(request, template)


def aboutUs(request):
    template = 'about.html'
    return render(request, template)