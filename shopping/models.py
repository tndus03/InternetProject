from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)  # 퍼즐 이름
    content = models.TextField()  # 퍼즐 설명
    price = models.IntegerField()  # 가격
    theme = models.CharField(max_length=30)  # 주제/테마
    countryM = models.CharField(max_length=30)  #제조국

    hook_text = models.CharField(max_length=100, blank=True)

    head_image = models.ImageField(upload_to='shopping/images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 포스팅한 날짜
    updated_at = models.DateTimeField(auto_now=True)  # 수정된 날짜

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/shopping/{self.pk}/'

    def get_number(self):
        return f'puzzle-{self.pk}'

    # 이미지, 제조사, 카테고리는 나중에