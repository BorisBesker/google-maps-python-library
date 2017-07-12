from django.core.urlresolvers import reverse
from django.test import TestCase

from mixins import CreateUserMixin
from users.forms import LoginForm, RegistrationForm


class RegistrationFormUnitTests(TestCase):
    def test_register_form_is_valid(self):
        form = RegistrationForm(data={'username': 'test_user', 'password1': 'pass1234', 'password2': 'pass1234'})
        self.assertTrue(form.is_valid())

    def test_register_form_is_invalid(self):
        form = RegistrationForm(data={'username': 'test_user', 'password1': 'pass1234', 'password2': 'pass123'})
        self.assertFalse(form.is_valid())


class LoginFormUnitTests(CreateUserMixin, TestCase):
    def test_login_form_is_valid(self):
        user = self.create_user('existing_user')
        form = LoginForm(data={'username': user.username, 'password': self.password})
        self.assertTrue(form.is_valid())

    def test_login_form_is_invalid(self):
        form = LoginForm(data={'username': 'non_existing_user', 'password': 'pass1234'})
        self.assertFalse(form.is_valid())


class UserRegistrationIntegrationTests(CreateUserMixin, TestCase):
    def test_redirection_on_register_successful(self):
        response = self.client.post(reverse('users:register'), {'username': 'new_user', 'password1': 'pass1234', 'password2': 'pass1234'})
        self.assertRedirects(response, reverse('users:login'))

    def test_register_successful(self):
        response = self.client.post(reverse('users:register'), {'username': 'new_user', 'password1': 'pass1234', 'password2': 'pass1234'})
        self.assertRedirects(response, reverse('users:login'))

    def test_register_unsuccessful(self):
        user = self.create_user('existing_user')
        response = self.client.post(reverse('users:register'), {'username': user.username, 'password1': 'pass1234', 'password2': 'pass1234'})
        self.assertTemplateUsed(response, 'registration.html')


class UserLoginIntegrationTests(CreateUserMixin, TestCase):
    def test_redirection_on_login_successful(self):
        user = self.create_user('existing_user')
        response = self.client.post(reverse('users:login'), {'username': user.username, 'password': self.password})
        self.assertRedirects(response, reverse('users:user-profile'))

    def test_login_unsuccessful(self):
        response = self.client.post(reverse('users:login'), {'username': 'non_existing_user', 'password': 'pass1234'})
        self.assertTemplateUsed(response, 'login.html')


class UserProfileIntegrationTests(CreateUserMixin, TestCase):
    def test_user_profile_page_with_authenticated_user(self):
        user = self.create_user('existing_user')
        self.client.post(reverse('users:login'), {'username': user.username, 'password': self.password})
        response = self.client.get(reverse('users:user-profile'))
        self.assertTemplateUsed(response, 'user-profile.html')


class AnonymousUserIntegrationTests(TestCase):
    def test_redirection_to_login_on_anonymous_user_access_profile_page(self):
        response = self.client.get(reverse('users:user-profile'))
        self.assertRedirects(
            response,
            '{redirect_path}?next={next_path}'.format(
                redirect_path=reverse('users:login'),
                next_path=reverse('users:user-profile')
            )
        )
