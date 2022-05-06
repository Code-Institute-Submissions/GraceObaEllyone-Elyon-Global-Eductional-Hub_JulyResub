from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from home.forms import ContactForm
from profiles.models import UserProfile


def index(request):

    template = 'home/index.html'

    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        contact_form = ContactForm(initial={"email": profile.default_email})
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }
    return render(request, template, context)


