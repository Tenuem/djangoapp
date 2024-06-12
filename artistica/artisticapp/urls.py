from django.urls import path
from .views import register, login_view, home, add_post, post_detail
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('', home, name='home'),
    path('add_post/', add_post, name='add_post'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
]