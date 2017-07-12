from page_objects import PageObject, PageElement


class LoginPage(PageObject):
    username = PageElement(name='username')
    password = PageElement(name='password')
    login_button = PageElement(class_name='login-register-button')
    error_message = PageElement(class_name='form-error')


class RegistrationPage(PageObject):
    username = PageElement(name='username')
    password = PageElement(name='password1')
    confirmation_password = PageElement(name='password2')
    registration_button = PageElement(class_name='login-register-button')
    username_error_message = PageElement(id_='username-error')
    password_error_message = PageElement(id_='password2-error')
