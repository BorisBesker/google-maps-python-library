from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView

from users.forms import RegistrationForm


class UserRegistration(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('users:register-successful')


class UserRegistrationSuccessful(TemplateView):
    template_name = 'registration_successful.html'
