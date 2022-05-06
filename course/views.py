from django.shortcuts import render, redirect, reverse, get_object_or_404

# Create your views here.
from .courseForms import CourseForm
from django.contrib import messages


def add_course(request):
    """
    ADD COURSE
    """

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'You added Course successfully!')

            if 'last_item' in request.sesion:
                del request.session['last_item']
            return redirect('single_course', args=[course.id])
        else:
            messages.error(request, 'Failed to add Course. Please check the information properly')

    form = CourseForm()

    template = 'course/add_course.html'

    context = {
        'form': form,
    }

    return render(request, template, context)

