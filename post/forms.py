from django.forms import ModelForm
from .models import Comment, Post, User


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields =[
            'comment_text',
        ]


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'tags',
            'image',
        ]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',

        ]