from instagram.models import CustomUser, Profile
from django.db.models.signals import post_save


def update_user_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(update_user_profile, sender = CustomUser)