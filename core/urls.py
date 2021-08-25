from django.urls import path

from .views import signup, index, user_login

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
]
