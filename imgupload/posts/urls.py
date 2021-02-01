from django.urls import path
from .views import HomePageView, CreatePostView

APP_NAME = 'posts'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post', CreatePageView.as_view(), name='add_post'),
]