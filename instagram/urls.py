from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from .import views

urlpatterns=[
    url('^$', views.home, name='home'),
    url('^login/$', LoginView.as_view(), name='login'),
    url('^logout/$', LogoutView.as_view(), name='logout'),
    url('^signup/$', views.signup, name='signup'),
    url('^insta/index/$', views.profile_info, name='profile')
]