import factory

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from users.forms import RegistrationForm


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'default_username'
    password = 'pass1234'


class RegistrationFormUnitTests(TestCase):
    def test_form_is_valid(self):
        form_data = {'username': 'testUser', 'password1': 'pass1234', 'password2': 'pass1234'}
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        form_data = {'username': 'testUser', 'password1': 'pass1234', 'password2': 'pass123'}
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())


class UserRegistrationIntegrationTests(TestCase):
    def test_redirection_on_register_successful(self):
        response = self.client.post(reverse('users:register'), {'username': 'user_1', 'password1': 'pass1234', 'password2': 'pass1234'})
        self.assertEqual(response.status_code, 302)

    def test_register_successful(self):
        response = self.client.post(reverse('users:register'), {'username': 'user_1', 'password1': 'pass1234', 'password2': 'pass1234'}, follow=True)
        self.assertIn('You successfully created a new account!', response.content)

    def test_register_unsuccessful(self):
        UserFactory(username='existing_user')
        response = self.client.post(reverse('users:register'), {'username': 'existing_user', 'password1': 'pass1234', 'password2': 'pass1234'})
        self.assertIn('A user with that username already exists.', response.content)
