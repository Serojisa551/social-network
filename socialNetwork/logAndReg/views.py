from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate  
from django.contrib.auth.forms import AuthenticationForm  


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("logAndReg:home")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="logAndReg/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("logAndReg:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="logAndReg/login.html", context={"login_form": form})


def home(request):
    return render(request=request, template_name='global/index.html')

#TODO It does not work correctly.
def reset_password(request):
    # Get the user's email address
    email = request.POST.get('email')

    # Generate a password reset link
    reset_link = 'http://yourwebsite.com/reset-password'

    # Send an email to the user with the password reset link
    send_mail(
        'Password Reset Request',
        'Click the following link to reset your password: {}'.format(
            reset_link),
        'your_gmail_address@gmail.com',
        [email],
        fail_silently=False,
    )

    # Redirect the user to a success page
    return render(request, 'logAndReg/resetPassword.html')
