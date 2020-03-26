from django.urls import path
from django.contrib.auth import views as auth_views # using django views for login and logout
from . import views

app_name = 'users'
urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), # login page
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'), # logout page
    path('register/', views.register, name='register'), # registration page
    path('profile/', views.profile, name='profile'), # profile page

]
