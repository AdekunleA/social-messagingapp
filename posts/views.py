from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(ListView):
    model = models.Post 
    template_name = 'post_list.html'
    
class PostDetailView(DetailView):
    model = models.Post  
    template_name = 'post_detail.html'
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Post 
    fields = ['message']
    template_name = 'post_edit.html'
    login_url = 'login'
    
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Post 
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    login_url = 'login'
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = models.Post 
    template_name = 'post_new.html'
    fields = ['message']
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


# Create your views here.
