# Create your views here.
message=''
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login,update_session_auth_hash
from django.contrib.auth.models import User
from django.http import HttpResponse
from . import models
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User=get_user_model()

# Global Variables
global_details=''

def indexPage(request):
    return render(request, 'homepage.html', {'global':global_details,'message':message})


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def contact_view(request):
    if request.method == 'POST':
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    return render(request, 'contact.html')

def terms_of_service_view(request):
    return render(request, 'terms_of_service.html')

def privacy_policy_view(request):
    return render(request, 'privacy_policy.html')

def shipping_information_view(request):
    return render(request, 'shipping_information.html')

def refund_policy_view(request):
    return render(request, 'refund_policy.html')

def about_us_view(request):
    return render(request, 'about_us.html')

def product_list_view(request):
    return render(request, 'product_list.html')

def product_detail_view(request, product_id):
    return render(request, 'product_detail.html', {'product_id': product_id})

@login_required
def profile_page_view(request):
    return render(request, 'profile_page.html')

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated successfully!')
            return redirect('profile_page') # Redirect back to the profile page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserChangeForm(instance=request.user) # Pre-fill form with current user data
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def password_change_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # Important! Keeps the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile_page') # Redirect back to profile or a success page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change.html', {'form': form})