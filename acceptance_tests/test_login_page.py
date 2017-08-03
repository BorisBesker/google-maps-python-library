from mixins import LoginMixin
from pages import LoginPage
from testcases import BaseTestCase


class LoginPageTestCase(LoginMixin, BaseTestCase):
    def setUp(self):
        super(LoginPageTestCase, self).setUp()
        self.driver.get(self.get_absolute_path(self.login_url))
        self.page = LoginPage(self.driver)

    def test_user_submitted_non_existing_username(self):
        self.authenticate_user('non_existing_user', 'pass1234')
        self.assertEqual(
            self.page.error_message.text,
            'Please enter a correct username and password. Note that both fields may be case-sensitive.'
        )
