from . import views
from django.urls import path
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view()),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('items/', views.ItemListView.as_view(), name='items'),
    path('user-details/', views.UserDetailCreateView.as_view(), name='user-details'),
    path('comments/', views.CommentCreateView.as_view(), name='comments'),
    ]