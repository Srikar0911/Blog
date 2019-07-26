from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from .forms import PostForm
from .models import Comment
from .forms import CommentForm
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
def comment_list(request,key):
    comments = get_list_or_404(Comment,key = key)
    return render(request, 'blog/comment_list.html', {'comments': comments})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.pen_name = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def comment_new(request,key):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # post.pen_name = request.user
            #post.published_date = timezone.now()
            comment.key = key
            comment.save()
            return redirect('comment_list', key = comment.key)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def comment_edit(request, pk,key):
    comment = get_object_or_404(Comment, pk = pk)
    if request.method == "COMMENT":
        form = CommentForm(request.COMMENT, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.key = key
            #post.published_date = timezone.now()
            comment.save()
            return redirect('comment_detail', pk= comment.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/post_comment.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return render(request, 'blog/comment_detail.html', {'comment': comment})