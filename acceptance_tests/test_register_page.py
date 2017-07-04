from urlparse import urljoin
from django.test import TestCase

from page_objects import PageObject, PageElement
from selenium import webdriver


class RegistrationPage(PageObject):
    username = PageElement(name='username')
    password = PageElement(name='password1')
    confirmation_password = PageElement(name='password2')
    registration_button = PageElement(class_name='submit-register')


class RegisterPageValidation(TestCase):
    HOST = 'http://127.0.0.1:8080/'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(urljoin(self.HOST, 'users/register'))
        self.page = RegistrationPage(self.driver)

    def test_user_submitted_existing_username(self):
        self.page.username = 'test'
        self.page.password = 'pass1234'
        self.page.confirmation_password = 'pass1234'
        self.page.registration_button.click()
        error_message = self.driver.find_element_by_id('username-error').text
        self.assertEqual(error_message, 'A user with that username already exists.')

    def test_user_submitted_too_short_passwords(self):
        self.page.username = 'new_user'
        self.page.password = 'pass123'
        self.page.confirmation_password = 'pass123'
        self.page.registration_button.click()
        error_message = self.driver.find_element_by_id('password2-error').text
        self.assertEqual(error_message, 'This password is too short. It must contain at least 8 characters.')

    def test_user_submitted_two_different_passwords(self):
        self.page.username = 'new_user'
        self.page.password = 'pass1234'
        self.page.confirmation_password = 'pass12345'
        self.page.registration_button.click()
        error_message = self.driver.find_element_by_id('password2-error').text
        self.assertEqual(error_message, "The two password fields didn't match.")

    def tearDown(self):
        self.driver.close()
