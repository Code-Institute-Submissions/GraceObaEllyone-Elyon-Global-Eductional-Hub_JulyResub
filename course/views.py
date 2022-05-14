from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404, reverse

# Create your views here.
from course.courseForm import CourseForm, CategoryForm
from course.models import Course


def all_course(request):
    course_list = Course.objects.all()

    paginator = Paginator(course_list, 6)
    page = request.GET.get('page')

    total = course_list.count()

    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    template = 'course/all_courses.html'

    context = {
        'courses': courses,
        'total': total
    }
    return render(request, template, context)


def single_course(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)

    context = {
        'course': course,

    }

    return render(request, 'course/single_course.html', context)


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            print(course.id)
            messages.success(request, "You added the Course successfully")

            if 'last_item' in request.session:
                del request.session['last_item']

            return redirect(reverse('single_course', args=[course.id]))

    form = CourseForm()
    template = 'course/add_course.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def edit_course(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, f'You updated {course.title}!')
            if 'last_item' in request.session:
                del request.session['last_item']

            return redirect(reverse('single_course', args=[course_pk]))
        else:
            messages.error(request, 'Failed to update Course. \
                Please ensure the form is valid.')
    else:
        form = CourseForm(instance=course)
        messages.info(
            request, f'You are editing a course details: {course.title}')

    template = 'course/edit_course.html'

    context = {
        'form': form,
        'course': course
    }

    return render(request, template, context)


def delete_course(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    course.delete()
    messages.success(request,
                     f'You deleted course: {course.title} from the database.')
    if 'last_item' in request.session:
        del request.session['last_item']


@login_required
def add_category(request):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Admin have access to the area.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, "You added the Category successfully")

            if 'last_item' in request.session:
                del request.session['last_item']

            return redirect(reverse('all_courses'))

    form = CategoryForm()
    template = 'course/add_category.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
