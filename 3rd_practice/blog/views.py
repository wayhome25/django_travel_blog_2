from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Comment, Post
from .forms import CommentForm

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'post_list' : post_list,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })

@login_required
def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(post) # NOTE: get_absolute_url 활용 (Post model)

    else:
        form = CommentForm() # NOTE: Create an instance of CommentForm class

    return render(request, 'blog/comment_form.html', {
        'form': form,
    })

@login_required
def comment_edit(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user:
        return redirect(comment.post)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment) # NOTE: instance 인자 필요
        if form.is_valid():
            form.save()
            return redirect(comment.post)

    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {
        'form': form,
    })

@login_required
def comment_delete(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user:
        return redirect(comment.post)

    if request.method == 'POST':
        comment.delete()
        return redirect(comment.post)

    return render(request, 'blog/comment_confirm_delete.html')
