from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^register/$', views.UserRegistration.as_view(), name='register'),
    url(r'^register-successful', views.UserRegistrationSuccessful.as_view(), name='register-successful')
]
