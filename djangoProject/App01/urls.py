from django.urls import path
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    # path('', views.home, name = 'App01-home'), #class based view leave as hompepage
    path('', PostListView.as_view(), name = 'App01-home'), #postlistview as hompepage
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail' ),  #pk = primary key
    path('about/', views.about, name = 'App01-about')
]   