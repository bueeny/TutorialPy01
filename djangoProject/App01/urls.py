from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    # path('', views.home, name = 'App01-home'), #class based view leave as hompepage
    path('', PostListView.as_view(), name = 'App01-home'), #postlistview as hompepage
    path('post/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail' ),  #pk = primary key
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update' ),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete' ), # update
    path('about/', views.about, name = 'App01-about'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create' ),
]   