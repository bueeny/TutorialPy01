from django.urls import path
from . import views
from .views import ProductListView

urlpatterns = [
    # path('', views.home, name = 'App01-home'), #class based view leave as hompepage
    path('Nanso/store', ProductListView.as_view(), name = 'store-home'),
]   