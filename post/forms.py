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
            'post_title',
            'post_content',
            'tags',
            'post_image',
        ]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',

        ]


# class TagForm(ModelForm):
#     class Meta:
#         model = Tag
#         fields = [
#             'tag_text',
#         ]