import factory

from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    password = factory.PostGenerationMethodCall('set_password', '')
