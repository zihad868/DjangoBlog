from django.urls import path
# from . import views
from .views import HomeView, ArticalDetail, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    # path('', views.home, name='home')
    path('',HomeView.as_view(), name='home'),
    path('artile-detail/<int:pk>', ArticalDetail.as_view(), name='artical-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-artical'),
    path('artical/<int:pk>/delete', DeletePostView.as_view(), name='delete-article'),
]