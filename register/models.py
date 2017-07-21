from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def upload_location(instance, filename):
    return '{}/{}'.format(instance.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(
        null=True,
        blank=True,
        help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    photo = models.ImageField(upload_to=upload_location, blank=True, null=True)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

