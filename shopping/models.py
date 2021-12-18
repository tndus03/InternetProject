from django.db import models
from django.contrib.auth.models import User
from markdownx.utils import markdown
from markdownx.models import MarkdownxField

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/shopping/category/{self.slug}'

    class Meta:
        verbose_name_plural = 'Categories'

class Make(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/shopping/make/{self.slug}'

class Post(models.Model):
    title = models.CharField(max_length=50)  # 퍼즐 이름
    content = MarkdownxField()  # 퍼즐 설명
    price = models.IntegerField()  # 가격
    theme = models.CharField(max_length=30)  # 주제/테마
    countryM = models.CharField(max_length=30)  #제조국

    hook_text = models.CharField(max_length=100, blank=True)

    head_image = models.ImageField(upload_to='shopping/images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 포스팅한 날짜
    updated_at = models.DateTimeField(auto_now=True)  # 수정된 날짜

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)  # 카테고리
    make = models.ForeignKey(Make, null=True, blank=True, on_delete=models.SET_NULL)  # 제조사

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/shopping/{self.pk}/'

    def get_number(self):
        return f'puzzle-{self.pk}'

    def get_content_markdown(self):
        return markdown(self.content)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return 'https://doitdjango.com/avatar/id/383/2df63151053cd6bc/svg/{{self.author.email}}/'