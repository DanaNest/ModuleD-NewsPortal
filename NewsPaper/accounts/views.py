from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SignUpForm


class SignUp(CreateView):
    form_class = SignUpForm
    model = User
    success_url = '/accounts/login/'
    template_name = 'registration/signup.html'
