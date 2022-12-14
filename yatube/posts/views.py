from .forms import PostForm
from .models import Post, Group, User
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    group = Group.objects.all()
    if request.user != post.author:
        return redirect('posts:post_detail', post.pk)
    is_edit = True
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
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


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.author = request.user
        form.save()
        return redirect(f'/profile/{form.author.username}/')
    return render(request, 'posts/post_create.html', {'form': form})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    user_posts = author.posts.filter(author=author)
    post_count = user_posts.count()
    paginator = Paginator(user_posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    title = f'Профайл пользователя {username}'
    context = {
        'title': title,
        'page_obj': page_obj,
        'post_count': post_count,
        'author': author,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    author_post = post.author
    post_count = Post.objects.filter(author=author_post).count()
    title = f'Пост {post.text[:30]}'
    context = {
        'post': post,
        'post_count': post_count,
        'title': title,
        'author_post': author_post,
    }
    return render(request, 'posts/post_detail.html', context)
