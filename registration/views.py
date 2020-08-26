from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CustomUserForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.postgres.search import SearchVector


def register(request):
    template_name = 'registration/register.html'
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        if user_form.is_valid():
            messages.success(request, ' Your account has been created. You may now log in')
            user_form.save()
            return redirect('profile_update')

    else:
        user_form = CustomUserForm()
    return render(request, template_name, {'user_form': user_form})


def user_login(request):
    template_name = 'registration/login.html'
    if request.user.is_authenticated():
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(request, 'home')

        else:
            messages.error(request, 'Wrong password or username or email. Please retry with the right credentials')
    return render(request, template_name)


def logout(request):
    template_name = 'registration/logout.html'
    auth.logout(request)
    return render(request, template_name)


@login_required()
def profile(request):
    template_name = 'registration/profile.html'
    return render(request, template_name)


@login_required()
def profile_update(request):
    template_name = 'registration/update_profile.html'
    if request.method == 'POST':
        prof_update_form = ProfileUpdateForm(request.POST, request.FILES, instance= request.user.profile)
        user_update_form = UserUpdateForm(request.POST, instance=request.user)

        if prof_update_form.is_valid() and user_update_form.is_valid():
            prof_update_form.save()
            user_update_form.save()
            messages.success(request,'Your account has been updates successfully')
            return redirect(reverse('profile'))
    else:
        prof_update_form = ProfileUpdateForm(instance=request.user.profile)
        user_update_form = UserUpdateForm(instance=request.user)
    context = {'user_update_form': user_update_form, 'prof_update_form': prof_update_form}

    return render(request, template_name, context)



