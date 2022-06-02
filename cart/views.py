from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from course.models import Course


def add_to_cart(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    redirect_url = request.POST.get('redirect_url')
    color = None

    print(redirect_url)
    # cart = request.session.get('cart', {})
    #
    # cart[course_id] = 1
    #
    # request.session['last_item'] = {
    #     'name': course.title,
    #     'image': course.courseImage
    # }
    #
    # request.session['cart'] = cart
    return redirect(redirect_url)


def view_cart(request):
    return render(request, 'cart.html')
