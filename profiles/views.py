from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.
from profiles.models import UserProfile
from profiles.forms import UserProfileForm, UserForm


def update_details(request):

    user = get_object_or_404(User, id=request.user.id)

    print(user.first_name + " " + user.last_name)

    profile = get_object_or_404(UserProfile, user=request.user)

    userForm = UserForm(instance=user)
    userProfileForm = UserProfileForm(instance=profile)

    context = {
        'userForm' : userForm,
        'userProfileForm': userProfileForm,
    }

    return render(request, 'update_profile.html', context)

