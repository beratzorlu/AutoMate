from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('blog', views.BlogList.as_view(), name='blog_list'),
    path('add-post/',  views.UserPostAdd.as_view(), name='url_post_add'),
    path('<slug:slug>/', views.DetailView.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.UserPostLike.as_view(), name='url_post_like'),  # noqa
    path('comment/<int:comment_id>/delete-comment/', views.delete_comment, name='delete_comment'),  # noqa
    path('comment/<int:comment_id>/edit-comment/', views.edit_comment, name='edit-comment'),  # noqa
    path('<slug:slug>/delete-post', views.UserPostDelete.as_view(), name='url_post_delete'),  # noqa
    path('<slug:slug>/edit-post', views.UserPostEdit.as_view(), name='url_post_edit'),  # noqa
]
