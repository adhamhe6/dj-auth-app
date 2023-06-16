from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create-post', views.create_post, name='create_post'),
]
