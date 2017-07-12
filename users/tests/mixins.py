from factories import UserFactory


class CreateUserMixin(object):
    password = 'pass1234'

    def create_user(self, username):
        return UserFactory(username=username, password=self.password)
