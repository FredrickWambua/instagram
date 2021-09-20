from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from .import views
from .views import PostCreateView


urlpatterns=[
    url('^$', views.home, name='home'),
    url('^login/$', LoginView.as_view(template_name='registration/login.html'), name='login'), 
    url('^logout/$', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url('^signup/$', views.signup, name='signup'),
    url('^insta/profile/$', views.profile, name='profile'),
    url('^insta/post/$', PostCreateView.as_view(), name ='post_add'),
    url('^search', views.search, name= 'search'),
    url('^createprofile/$', views.createprofile, name = 'createprofile'),

]