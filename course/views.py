from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404

# Create your views here.
from .courseForms import CourseForm
from django.contrib import messages


@login_required
def add_course(request):
    """
    ADD COURSE
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry only the admin can add access this')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'You added Course successfully!')

            if 'last_item' in request.sesion:
                del request.session['last_item']
            #return redirect('single_course', args=[course.id])
        else:
            messages.error(request, 'Failed to add Course. Please check the information properly')

    form = CourseForm()

    template = 'add_course.html'

    context = {
        'form': form,
    }

    return render(request, template, context)

