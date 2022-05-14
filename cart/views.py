from django.shortcuts import render, get_object_or_404

# Create your views here.
from course.models import Course


def add_to_cart(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    redirect_url = request.POST.get('redirect_url')
    color = None

    cart = request.session.get('cart', {})
