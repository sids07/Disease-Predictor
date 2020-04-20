from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.conf import settings
from django.core.mail import send_mail
from django.db import transaction


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'YOUR ACCOUNT HAS BEEN CREATED!YOU ARE ABLE TO LOGIN NOW')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
@transaction.atomic
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request,
                f'Your profile has been updated successfully'
            )
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


"""
class  receive:
    if request.method == 'POST':
        #form or something to direct the flow
        if form.is_valid():
            save_it= form.save()
            save_it.save()
            messages.success(request, f'confirmation of reservation sent to your email')
            return redirect('Here we need direct somewhere after successfull reservation')
    else:
         #form or something to direct the flow
    
    return render(request,'')
    """