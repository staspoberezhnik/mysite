from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
# from . import filters
from .filters import PostFilter
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from .forms import CommentForm, PostForm
# Create your views here.


class AllPostView(ListView):

    template_name = 'home_page.html'
    model = Post
    context_object_name = 'post_list'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.all().order_by("-date_created")

    def get_context_data(self, **kwargs):

        context = super(AllPostView, self).get_context_data(**kwargs)
        username = None
        if self.request.user.is_staff\
            or self.request.user.is_superuser\
                or self.request.user.is_authenticated:
            username = auth.get_user(self.request).username

        page_request_var = 'page'

        context['username'] = username
        context['page_request_var'] = page_request_var
        return context


# def post_list(request):
#     username = None
#     if request.user.is_staff or request.user.is_superuser or request.user.is_authenticated:
#         username = auth.get_user(request).username
#
#     query_post_list = Post.objects.all().order_by("-date_created")
#     paginator = Paginator(query_post_list, 10)  # Show 10  per page
#     page_request_var = 'page'
#     page = request.GET.get(page_request_var)
#
#     try:
#         queryset = paginator.page(page)
#     except PageNotAnInteger:
#         queryset = paginator.page(1)
#     except EmptyPage:
#         queryset = paginator.page(paginator.num_pages)
#
#     context = {
#         'post_list': queryset,
#         'username': username,
#         'page_request_var': page_request_var,
#     }
#     return render(request, 'home_page.html', context)

class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'post_creation_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        form.save_m2m()
        return redirect(instance.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context

    def form_invalid(self, form):
        return redirect('post: post_create')

# def post_create(request):
#     user = request.user
#     form = PostForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user = User.objects.get(id=user.pk)
#         instance.save()
#         form.save_m2m()
#         return HttpResponseRedirect(instance.get_absolute_url())
#     context = {
#         "form": form,
#         'username': auth.get_user(request).username,
#     }
#     return render(request, 'post_creation_form.html', context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    user = request.user
    if request.user.is_staff or\
            request.user.is_superuser or\
            request.user.is_authenticated:
        username = auth.get_user(request).username
    else:
        username = None

    if instance.user_id == user.pk:
        if request.POST:
            form = PostForm(request.POST or None,
                            request.FILES or None, instance=instance)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                form.save_m2m()
                return HttpResponseRedirect(instance.get_absolute_url())
            else:
                return redirect('post:edit_post', id=id)
        else:
            form = PostForm(instance=instance)
            context = {
                "instance": instance,
                "form": form,
                'username': username,
            }
        return render(request, 'post_creation_form.html', context)
    else:
        return redirect('post:home')


def post_detail(request, id):
    post_instance = get_object_or_404(Post, id=id)
    comment_instance = Comment.objects.filter(post_to_id=id)
    user = request.user
    comment_form = None
    username = None
    tag_form = None
    can_edit = None
    can_delete = None

    if request.user.is_staff or\
            request.user.is_superuser or\
            request.user.is_authenticated:
        username = auth.get_user(request).username
        comment_form = CommentForm()

    if post_instance.user_id == user.pk:
        can_edit = True
        can_delete = True
    else:
        post_instance.views_count += 1

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
    return render(request, 'post_detail.html', context)


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


class PostByTags(AllPostView):
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['tag']).order_by("-date_created")

# def post_by_tags(request, tag):
#     username = None
#     if request.user.is_staff or request.user.is_superuser or request.user.is_authenticated:
#         username = auth.get_user(request).username
#
#     query_post_list = Post.objects.filter(tags__slug=tag).order_by("-date_created")
#     paginator = Paginator(query_post_list, 10)  # Show 10  per page
#     page_request_var = 'page'
#     page = request.GET.get(page_request_var)
#
#     try:
#         queryset = paginator.page(page)
#     except PageNotAnInteger:
#         queryset = paginator.page(1)
#     except EmptyPage:
#         queryset = paginator.page(paginator.num_pages)
#
#     context = {
#         'post_list': queryset,
#         'username': username,
#         'page_request_var': page_request_var,
#     }
#     return render(request, 'home_page.html', context)


def users_list(request):
    users_lists = User.objects.all()
    context = {
        'users': users_lists,
        'username': auth.get_user(request).username,
    }
    return render(request, 'users_list.html', context)


class UserPostListView(AllPostView):
    paginate_by = 10

    def get_queryset(self):
        queryset = PostFilter(self.request.GET,
                              queryset=Post.objects.
                              filter(user_id=self.kwargs['id']).
                              order_by("-date_created"))
        return queryset.qs

    def get_context_data(self, **kwargs):
        context = super(UserPostListView, self).get_context_data(**kwargs)
        model_filtered = PostFilter(self.request.GET,
                                    queryset=Post.objects.
                                    filter(user_id=self.kwargs['id']).
                                    order_by("-date_created"))
        context['filter'] = model_filtered
        return context


# def user_post_list(request, id):
#
#     username = None
#     if request.user.is_staff or request.user.is_superuser or request.user.is_authenticated:
#         username = auth.get_user(request).username
#
#     post_filtered = PostFilter(
#         request.GET,
#         queryset=Post.objects.filter(user_id=id).order_by("-date_created")
#     )
#
#     paginator = Paginator(post_filtered.qs, 5)  # Show 10  per page
#     page_request_var = 'page'
#     page = request.GET.get(page_request_var)
#
#     try:
#         queryset = paginator.page(page)
#     except PageNotAnInteger:
#         queryset = paginator.page(1)
#     except EmptyPage:
#         queryset = paginator.page(paginator.num_pages)
#
#     context = {
#         'filter': post_filtered,
#         'post_list': queryset,
#         'username': username,
#         'page_request_var': page_request_var,
#     }
#     return render(request, 'home_page.html', context)


def user_comments_list(request, id):
    comments_list = Comment.objects.filter(user_left_id=id)
    post_list = Post.objects.filter(user_id=id)
    context = {
        'posts': post_list,
        'comments': comments_list,
        'username': auth.get_user(request).username,
    }
    return render(request, 'comments_list.html', context)


def post_delete(request, id):
    instance = get_object_or_404(Post, id=id)
    user = request.user
    if request.user.is_staff or request.user.is_superuser or request.user.is_authenticated:
        username = auth.get_user(request).username
    else:
        username = None
    if instance.user_id == user.pk:
        if request.POST:
            Post.objects.get(id=id).delete()
            return redirect('/')
        else:
            context = {
                'post': instance,
                'username': username,
            }
            return render(request, 'post_delete_form.html', context)
    else:
        return redirect('post:home')

