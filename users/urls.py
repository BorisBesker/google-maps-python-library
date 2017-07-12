from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^login/$', views.UserLogin.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    url(r'^register/$', views.UserRegistration.as_view(), name='register'),
    url(r'^user-profile', views.UserProfilePage.as_view(), name='user-profile')
]
