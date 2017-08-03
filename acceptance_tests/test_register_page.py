from django.core.urlresolvers import reverse

from pages import RegistrationPage
from testcases import BaseTestCase
from users.tests.mixins import CreateUserMixin


class RegisterPageTestCase(CreateUserMixin, BaseTestCase):
    register_url = reverse('users:register')

    def setUp(self):
        super(RegisterPageTestCase, self).setUp()
        self.driver.get(self.get_absolute_path(self.register_url))
        self.page = RegistrationPage(self.driver)

    def fill_registration_form(self, username, password, confirmation_password=None):
        self.page.username.send_keys(username)
        self.page.password.send_keys(password)
        self.page.confirmation_password.send_keys(confirmation_password or password)
        self.page.registration_button.click()

    def test_user_submitted_existing_username(self):
        user = self.create_user('existing_user')
        self.fill_registration_form(user.username, self.password)
        self.assertEqual(self.page.username_error_message.text, 'A user with that username already exists.')

    def test_user_submitted_too_short_passwords(self):
        self.fill_registration_form('new_user', 'pass123')
        self.assertEqual(self.page.password_error_message.text, 'This password is too short. It must contain at least 8 characters.')

    def test_user_submitted_two_different_passwords(self):
        self.fill_registration_form('new_user', 'pass1234', 'pass12345')
        self.assertEqual(self.page.password_error_message.text, "The two password fields didn't match.")
