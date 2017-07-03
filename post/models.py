from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone


def upload_location(instance, filename):
    return '{}/{}'.format(instance.id, filename)


class Post(models.Model):

    post_title = models.CharField(max_length=120)
    post_content = models.TextField()
    post_user = models.ForeignKey(User)
    post_image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    post_date_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    # post_date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={"id": self.id})


class Tag(models.Model):

    tag_text = models.CharField(max_length=30, verbose_name='Tag text' )
    tag_post = models.ForeignKey(Post)

    def __str__(self):
        return self.tag_text


class Comment(models.Model):

    comment_text = models.TextField()
    post_to = models.ForeignKey(Post)
    user_left = models.ForeignKey(User)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.comment_text

