from django.core.urlresolvers import reverse

from mixins import LoginMixin
from testcases import BaseTestCase
from test_login_page import LoginPage
from users.tests.mixins import CreateUserMixin


class UserProfilePageTestCase(CreateUserMixin, LoginMixin, BaseTestCase):
    logout_url = reverse('users:logout')
    user_profile_url = reverse('users:user-profile')

    def setUp(self):
        super(UserProfilePageTestCase, self).setUp()
        self.page = LoginPage(self.driver)

    def test_anonymous_user_accessing_user_profile_page(self):
        self.driver.get(self.get_absolute_path(self.user_profile_url))
        page_title = self.driver.find_element_by_tag_name('h1').text
        form_identifier = self.driver.find_element_by_tag_name('form').get_attribute('id')
        self.assertEqual(page_title, 'Sign in')
        self.assertEqual(form_identifier, 'login')

    def test_authenticated_user_accessing_user_profile_page(self):
        user = self.create_user('existing_user')
        self.authenticate_user(user.username, self.password)
        self.driver.get(self.get_absolute_path(self.user_profile_url))
        message = self.driver.find_element_by_tag_name('p').text
        logout_link = self.driver.find_element_by_tag_name('a').get_attribute('href')
        self.assertEqual(message, 'You are logged in!')
        self.assertEqual(logout_link, self.get_absolute_path(self.logout_url))
