from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# from django.utils import timezone
from taggit.managers import TaggableManager


def upload_location(instance, filename):
    return '{}/{}'.format(instance.id, filename)


class Post(models.Model):

    title = models.CharField(max_length=120)
    content = models.TextField()
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    date_created = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(blank=True, default=0)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={"id": self.id})


class Comment(models.Model):

    comment_text = models.TextField()
    post_to = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_left = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text
