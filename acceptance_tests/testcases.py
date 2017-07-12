from urlparse import urljoin

from django.test import LiveServerTestCase
from selenium import webdriver


class BaseTestCase(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    @classmethod
    def get_absolute_path(cls, relative_path):
        return urljoin(cls.live_server_url, relative_path)
