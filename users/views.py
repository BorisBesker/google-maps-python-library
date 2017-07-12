from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, FormView, RedirectView, TemplateView

from users.forms import LoginForm, RegistrationForm


class UserRegistration(SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    success_message = 'You successfully created your account, now you can sing in!'
    template_name = 'registration.html'

    def get_success_url(self):
        return reverse('users:login')


class UserLogin(FormView):
    form_class = LoginForm
    success_url = reverse_lazy('users:user-profile')
    template_name = 'login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(UserLogin, self).form_valid(form)


class UserProfilePage(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users:login')
    template_name = 'user-profile.html'


class Logout(RedirectView):
    url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).get(request, *args, **kwargs)
