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
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from .serializers import * 
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


# Working only with Swagger
@swagger_auto_schema(method='post', request_body=RegisterSerializer)
@api_view(['POST'])
def registration(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        messages.success(request, f"New account created: {user.username}")
        return Response({"message": "User successfully registered"})
    return Response(serializer.errors, status=400)


# Working only with Swagger
@swagger_auto_schema(method='post', request_body=LoginSerializer)
@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        messages.info(request, f"You are now logged in as {user.username}.")
        return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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
#                     #     (F'sent message to {message} Message Id: {message["id"]}')
#                     # except HTTPError as error:
#                     #     (F'An error occurred: {error}')
#                     #     message = None
#                     # return redirect("/password_reset/done/")
#     password_reset_form = PasswordResetForm()
#     return render(request=request, template_name="passwordReset/passwordReset.html", context={"passwordResetForm": password_reset_form})
