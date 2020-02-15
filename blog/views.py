from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.conf import settings

class HomePageView (ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'

class AboutPageView (TemplateView):
    template_name = 'about.html'

class PostPageView (DetailView):
    model = Post
    template_name = 'posts.html'

class BlogCreateView (CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'text']

class BlogUpdateView (UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'text']

class BlogDeleteView (DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('homepage')