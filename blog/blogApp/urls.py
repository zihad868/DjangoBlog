from django.urls import path
# from . import views
from .views import HomeView, ArticalDetail, AddPostView

urlpatterns = [
    # path('', views.home, name='home')
    path('',HomeView.as_view(), name='home'),
    path('artical-detail/<int:pk>', ArticalDetail.as_view(), name='artical-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
]