from django.shortcuts import render, redirect
from django.contrib import messages # django messages for certain actions
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required # decorator for auth

#view for registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created successfuly')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# view for profile
@login_required
def profile(request):
    return render(request, 'profile.html')
