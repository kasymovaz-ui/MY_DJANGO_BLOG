from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from django.urls import reverse_lazy

# Category Views
class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category_list.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/category_detail.html'

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'blog/category_form.html'

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'blog/category_form.html'

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')
    template_name = 'blog/category_confirm_delete.html'

# Post Views
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'text', 'categories']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'text', 'categories']
    template_name = 'blog/post_form.html'

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'blog/post_confirm_delete.html'
