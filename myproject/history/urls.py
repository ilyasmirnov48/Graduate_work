from django.urls import path

from .views import index, stories, video, photo, RegisterUser, logout_user, LoginUser, \
    ShowPost, StoriesCategory

urlpatterns = [
    path('', index, name='home'),
    path('stories', stories, name='stories'),
    path('video', video, name='video'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('photo', photo, name='photo'),
    path('post/<int:post_id>/', ShowPost.as_view(), name='post'),
    path('category/<int:cat_id>/', StoriesCategory.as_view(), name='category'),
]
