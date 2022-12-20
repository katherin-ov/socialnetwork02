from .forms import PostForm
from .models import Post, Group, User
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

LIMIT = 10


def post_sort(queryset, request):
    paginator = Paginator(queryset, LIMIT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return {
        'paginator': paginator,
        'page_number': page_number,
        'page_obj': page_obj,
    }


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    context = {
        'posts': post_list,
    }
    context.update(post_sort(post_list, request))
    return render(request, 'posts/index.html', context)


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    group = Group.objects.all()
    if not request.user.is_authenticated:
        return redirect('/posts/<post_id>/')
    if request.user != post.author:
        return redirect('posts:post_detail', pk=post_id)
    is_edit = True
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:post_detail', post.pk)
    form = PostForm(instance=post)
    context = {
        'form': form,
        'is_edit': is_edit,
        'group': group,
        'post_id': post.pk,
    }
    return render(request, 'posts/post_create.html', context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    template_name = 'posts/post_create.html'
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:profile', username=post.author.username)
    return render(request, template_name, {'form': form})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all()
    context = {
        'group': group,
    }
    context.update(post_sort(post_list, request))
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    user_posts = author.posts.all()
    post_count = user_posts.count()
    context = {
        'post_count': post_count,
        'user_posts': user_posts,
        'author': author,
    }
    context.update(post_sort(user_posts, request))
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    author_post = post.author
    post_count = Post.objects.filter(author=author_post).count()
    context = {
        'post': post,
        'post_count': post_count,
    }
    return render(request, 'posts/post_detail.html', context)
