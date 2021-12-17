from django.shortcuts import render
from .models import Post, Category, Make
from django.views.generic import ListView, DetailView

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

    # def make_get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(PostList, self).get_context_data()
    #     context['makes'] = Make.objects.all()
    #     return context

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        # context['comment_form'] = CommentForm
        return context