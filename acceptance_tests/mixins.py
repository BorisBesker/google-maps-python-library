from django.core.urlresolvers import reverse


class LoginMixin(object):
    login_url = reverse('users:login')

    def authenticate_user(self, username, password):
        self.driver.get(self.get_absolute_path(self.login_url))
        self.page.username.send_keys(username)
        self.page.password.send_keys(password)
        self.page.login_button.click()
