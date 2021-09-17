from os import name
from django.test import TestCase
from .models import Comment, Profile, Post
from django.contrib.auth.models import User

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(email='wambua@g.com')
        self.user.save()

        self.test_profile = Profile(id=1, name='wambua', email='wambua@g.com',)

    def test_instance(self):
        self.assertTrue(isinstance(self.test_profile, Profile))

    def test_save_profile(self):
        self.profile_test.save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)> 0)

class TestPost(TestCase):
    def setUp(self):
        self.test_user_post = Profile(name='wambua', user=User(name='wambua'))
        self.test_user_post.save()
        
        self.post_test = Post(name='cycle', user=self.test_user_post)

    def test_instance(self):
        self.assertTrue(isinstance(self.post_test), Post)

    def test_save_post(self):
        self.post_test.save()
        posts = Post.objects.all()
        self.assertTrue(len(posts)>0)

    def test_delete_post(self):
        self.post_test.delete()
        posts = Post.objects.all()
        self.assertTrue(len(posts)<1)