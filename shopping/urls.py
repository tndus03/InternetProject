from django.urls import path
from . import views

urlpatterns = [    # 서버IP/shopping/
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('make/<str:slug>/', views.make_page),
    path('category/<str:slug>/', views.category_page), # 서버IP/shopping/category/slug
    path('<int:pk>/new_comment/', views.new_comment),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]