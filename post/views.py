from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# from . import filters
from .filters import PostFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from .forms import CommentForm, PostForm
# Create your views here.


def post_list(request):
    username = None
    if request.user.is_staff or request.user.is_superuser or request.user.is_authenticated:
        username = auth.get_user(request).username

    query_post_list = Post.objects.all().order_by("-post_date_created")
    paginator = Paginator(query_post_list, 10)  # Show 10  per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'post_list': queryset,
        'username': username,
        'page_request_var': page_request_var,
    }
    return render(request, 'home.html', context)


def post_create(request):
    user = request.user
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.post_user = User.objects.get(id=user.pk)
        instance.save()
        form.save_m2m()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        'username': auth.get_user(request).username,
    }
    return render(request, 'post_form.html', context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "form": form,
        'username': auth.get_user(request).username,
    }
    return render(request, 'post_form.html', context)


def post_detail(request, id):
    post_instance = get_object_or_404(Post, id=id)
    comment_instance = Comment.objects.filter(post_to_id=id)
    user = request.user
    comment_form = None
    username = None
    tag_form = None
    can_edit = None
    can_delete = None
    post_instance.views_count += 1

    if request.user.is_staff or request.user.is_superuser or request.user.is_authenticated:
        username = auth.get_user(request).username
        comment_form = CommentForm


    if post_instance.post_user_id == user.pk:
        can_edit = True
        can_delete = True
        post_instance.views_count -= 1

    post_instance.save()

    context = {
        'post_instance': post_instance,
        'comment_instance': comment_instance,
        'form': comment_form,
        'username': username,
        'tag_form': tag_form,
        'can_edit': can_edit,
        'can_delete': can_delete,
    }
    return render(request, 'detail.html', context)


def add_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            user = request.user
            comment = form.save(commit=False)
            comment.post_to = Post.objects.get(id=id)
            comment.user_left = User.objects.get(id=user.pk)
            form.save()
    return redirect(post.get_absolute_url())


def post_by_tags(request, tag):
    username = None
    if request.user.is_staff or request.user.is_superuser or request.user.is_authenticated:
        username = auth.get_user(request).username

    query_post_list = Post.objects.filter(tags__slug=tag).order_by("-post_date_created")
    paginator = Paginator(query_post_list, 10)  # Show 10  per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'post_list': queryset,
        'username': username,
        'page_request_var': page_request_var,
    }
    return render(request, 'home.html', context)


def users_list(request):
    users_lists = User.objects.all()
    context = {
        'users': users_lists,
        'username': auth.get_user(request).username,
    }
    return render(request, 'users_list.html', context)


def user_post_list(request, id):

    username = None
    if request.user.is_staff or request.user.is_superuser or request.user.is_authenticated:
        username = auth.get_user(request).username

    post_filtered = PostFilter(
        request.GET,
        queryset=Post.objects.filter(post_user_id=id).order_by("-post_date_created")
    )

    # query_post_list = Post.objects.filter(post_user_id=id).order_by("-post_date_created")
    paginator = Paginator(post_filtered.qs, 5)  # Show 10  per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'filter': post_filtered,
        'post_list': queryset,
        'username': username,
        'page_request_var': page_request_var,
    }
    return render(request, 'home.html', context)


def user_comments_list(request, id):
    comments_list = Comment.objects.filter(user_left_id=id)
    post_list = Post.objects.filter(post_user_id=id)
    context = {
        'posts': post_list,
        'comments': comments_list,
        'username': auth.get_user(request).username,
    }
    return render(request, 'comments_list.html', context)


def post_delete(request, id):
    Post.objects.get(id=id).delete()
    Comment.objects.filter(post_to_id=id).delete()
    return redirect('/')
