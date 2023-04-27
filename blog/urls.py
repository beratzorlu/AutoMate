from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.DetailView.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.UserPostLike.as_view(), name='url_post_like')
]
