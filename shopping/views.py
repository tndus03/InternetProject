from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from .models import Post, Category, Make
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm
from django.shortcuts import get_object_or_404

# Create your views here.
def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'price', 'theme', 'countryM', 'hook_text', 'content', 'head_image', 'category', 'make']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(PostCreate, self).form_valid(form)
            # tags_str = self.request.POST.get('tags_str')
            # if tags_str:
            #     tags_str = tags_str.strip()
            #     tags_str = tags_str.replace(',', ';')
            #     tags_list = tags_str.split(';')
            #     for t in tags_list:
            #         t = t.strip()
            #         tag, is_tag_created = Tag.objects.get_or_create(name=t)
            #         if is_tag_created:
            #             tag.slug = slugify(t, allow_unicode=True)
            #             tag.save()
            #         self.object.tags.add(tag)
            return response
        else:
            return redirect('/shopping/')

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'price', 'theme', 'countryM', 'hook_text', 'content', 'head_image', 'category', 'make']

    template_name = 'shopping/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author :
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else :
            raise PermissionDenied

class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

    def make_get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).make_get_context_data()
        context['makes'] = Make.objects.all()
        context['unknown_make'] = Post.objects.filter(make=None).count()
        return context

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        return context

    def make_get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).make_get_context_data()
        context['makes'] = Make.objects.all()
        context['unknown_make'] = Post.objects.filter(make=None).count()
        return context

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(request, 'shopping/post_list.html',
                  {
                      'post_list' : post_list,
                      'categories' : Category.objects.all(),
                      'no_category_post_count' : Post.objects.filter(category=None).count(),
                      'category' : category
                  }
                  )

def make_page(request, slug):
    if slug == 'unknown_make':
        make = '미상'
        post_list = Post.objects.filter(make=None)
    else:
        make = Make.objects.get(slug=slug)
        post_list = Post.objects.filter(make=make)

    return render(request, 'shopping/post_list.html',
                  {
                      'post_list' : post_list,
                      'makes' : Make.objects.all(),
                      'unknown_make' : Post.objects.filter(make=None).count(),
                      'make' : make
                  }
                  )