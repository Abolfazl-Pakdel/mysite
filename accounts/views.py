from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
# Create your views here.
# def login_view(request):
#     if not request.user.is_authenticated:
#         if request.method == "POST":
#             form = AuthenticationForm(request=request,data=request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data.get('username')
#                 password = form.cleaned_data.get('password')
#
#                 try:
#                     user_obj = User.objects.get(email=username)
#                     username = user_obj.username
#                 except User.DoesNotExist:
#                     pass
#                 user = authenticate(request, username=username, password=password)
#
#                 if user is not None:
#                     login(request, user)
#                     return redirect('/')
#         form = AuthenticationForm()
#         context = {'form': form}
#         return render(request, 'accounts/login.html', context)
#     else:
#         return redirect('/')

def login_view(request):
    if not request.user.is_authenticated:

        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            # بررسی اینکه ورودی ایمیل است یا یوزرنیم
            try:
                user_obj = User.objects.get(email=username)
                username = user_obj.username
            except User.DoesNotExist:
                pass

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect('/')

        return render(request, 'accounts/login.html')

    else:
        return redirect('/')

# ==============================
@login_required(redirect_field_name='')
def logout_view(request):
    logout(request)
    return redirect('/')

# ==============================
def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = CustomUserCreationForm()
        context = {'form': form}
        return  render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')