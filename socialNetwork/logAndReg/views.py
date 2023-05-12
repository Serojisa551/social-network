from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
from django.contrib.auth.forms import UserCreationForm
import base64

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("logAndReg:home")
        else:
            messages.error(request, "Account creation failed")

    form = NewUserForm()
    return render(request, "logAndReg/register.html", {"form": form})



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

#TODO Works incorrectly
# def password_reset_request(request):
#     if request.method == "POST":
#         password_reset_form = PasswordResetForm(request.POST)
#         if password_reset_form.is_valid():
#             data = password_reset_form.cleaned_data['email']
#             associated_users = User.objects.filter(Q(email=data))
#             if associated_users.exists():
#                 for user in associated_users:
#                     subject = "Password Reset Requested"
#                     email_template_name = "passwordReset/passwordResetEmail.txt"
#                     c = {
#                         "email": user.email,
#                         'domain': '127.0.0.1:8000',
#                         'site_name': 'Website',
#                         "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                         "user": user,
#                         'token': default_token_generator.make_token(user),
#                         'protocol': 'http',
#                     }
#                     email = render_to_string(email_template_name, c)
#                     try:
#                         send_mail(subject, email, 'Isahakyan2021@gmail.com',
#                                   [user.email], fail_silently=False)
#                     except BadHeaderError:
#                         return HttpResponse('Invalid header found.')
#                     # SCOPES = [
#                     #         "https://www.googleapis.com/auth/gmail.send"
#                     #     ]
#                     # flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#                     # creds = flow.run_local_server(port=0)

#                     # service = build('gmail', 'v1', credentials=creds)
#                     # message = MIMEText('This is the body of the email')
#                     # message['to'] = 'recipient@gmail.com'
#                     # message['subject'] = 'Email Subject'
#                     # create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

#                     # try:
#                     #     message = (service.users().messages().send(userId="me", body=create_message).execute())
#                     #     print(F'sent message to {message} Message Id: {message["id"]}')
#                     # except HTTPError as error:
#                     #     print(F'An error occurred: {error}')
#                     #     message = None
#                     # return redirect("/password_reset/done/")
#     password_reset_form = PasswordResetForm()
#     return render(request=request, template_name="passwordReset/passwordReset.html", context={"passwordResetForm": password_reset_form})
