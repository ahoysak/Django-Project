from django.urls import path
from .views import HomeView, AddPostView, UpdatePostView, PostDetailView, DeletePostView, CategoryView, LikeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('new-post/', AddPostView.as_view(), name='new_post'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/update/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:select>/', CategoryView,  name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),
]

