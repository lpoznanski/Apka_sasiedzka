from . import views
from django.urls import path
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view()),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    ]