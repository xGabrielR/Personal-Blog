from .models import Post
from comments.forms import CommentForm
from comments.models import Comment
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView

class PostIndex(ListView):
    model = Post
    paginate_by = 3
    context_object_name = 'posts'
    template_name = 'posts/index.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('icon')
        qs = qs.order_by('-created').filter(published=True)
    
        return qs

class PostCategory(PostIndex):
    template_name = 'posts/category.html'
    
    def get_queryset(self):
        qs = super().get_queryset()

        category = self.kwargs.get('category', None)

        if not category:
            return qs

        qs = qs.filter(category__name__iexact=category)

        return qs

class PostDetail(UpdateView):
    model = Post
    form_class = CommentForm
    context_object_name = 'post'
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comm = Comment.objects.filter(published=True, post=post.id)

        context['comments'] = comm
        
        return context

    def form_valid(self, form):
        post = self.get_object()
        comment = Comment(**form.cleaned_data)

        comment.post = post
        if self.request.user.is_authenticated:
            comment.user = self.request.user

        comment.save()

        return redirect('detail', slug=post.slug)