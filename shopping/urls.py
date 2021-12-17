from django.urls import path
from . import views

urlpatterns = [    # 서버IP/shopping/
    path('category/<str:slug>/', views.category_page), # 서버IP/shopping/category/slug
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]