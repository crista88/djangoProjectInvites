from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from djangoProjectInvites.settings import EMAIL_HOST_USER
from userextend.forms import UserForm


# Create your views here.
class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()

            new_user.last_name = new_user.last_name.title()
            new_user.username = new_user.first_name + new_user.last_name

            details_user = {
                'full_name': f'{new_user.first_name} {new_user.last_name}',
                'username': new_user.username
            }
            # subject = 'New account confirmation'
            # message = get_template('mail.html').render(details_user)
            # mail = EmailMessage(subject, message, EMAIL_HOST_USER, [new_user.email])
            # mail.content_subtype = 'html'
            # mail.send()

            new_user.save()
            return super(UserCreateView, self).form_valid(form)