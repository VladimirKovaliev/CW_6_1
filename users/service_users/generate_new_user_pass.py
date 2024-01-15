from django.shortcuts import redirect
from django.urls import reverse

from users.service_users.generate_password import password_generator
from users.service_users.send_emails import send_new_password


# from users.service_users1 import password_generator, send_new_password


def generate_new_password(request):
    new_password = password_generator(size=12)
    send_new_password(new_password, request.user.email)
    if request.user.is_authenticated:
        request.user.set_password(new_password)
        request.user.save()
        return redirect(reverse('users:profile'))