from instagram.models import User, Profile
from django.db.models.signals import post_save


def update_user_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(update_user_profile, sender = User)