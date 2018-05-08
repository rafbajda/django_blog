from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from comments.forms import CreateComment


def add_comment_to_post(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == "POST":
        form = CreateComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('articles:list')
    else:
        form = CreateComment()
    return render(request, 'comments/add_comment.html', {'form': form})