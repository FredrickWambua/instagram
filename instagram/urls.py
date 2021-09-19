from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from .import views
from .views import PostCreateView


urlpatterns=[
    url('^$', views.home, name='home'),
    url('^login/$', LoginView.as_view(), name='login'), 
    url('^logout/$', LogoutView.as_view(), name='logout'),
    url('^signup/$', views.signup, name='signup'),
    url('^insta/profile/<username>/$', views.profile, name='profile'),
    url('^insta/post/$', PostCreateView.as_view(), name ='post_add'),
    url('^search', views.search, name= 'search'),

]