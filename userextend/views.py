from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from djangoProjectInvites.settings import EMAIL_HOST_USER
from userextend.forms import UserForm


# Create your views here.
class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm

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
            login(self.request, new_user)
            return redirect('dashboard_home')
        return super().form_valid(form)

# pct valid la Radu..dupa ce ma loghez daca dau back in browser ma duce inapoi p pag de log in desii user e authentificat
# leg cu cache-ul poate ? in mod normal javascript pt a nu mai memora cache-ul :( sau poate vreun model(clasa) cu python???
# intreaba-l pe Daniel!!

### Daniel zice asa:
# in django core este un model cache care face exact asta, def o clasa de log in cache cu un OK si un timeut, 2 fc principale get si set
# in models.py faci asta
class UserLoginView(View):
    template_name = 'registration/login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard_home')
        return render(request, self.template_name, {'form': form})