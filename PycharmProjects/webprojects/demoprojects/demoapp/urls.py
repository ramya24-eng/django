from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#from accounts.views import UserCreateView



urlpatterns = [
    path('', views.home, name='home'),
    path('profile/',views.profile, name='profile'),
    #path('login/',UserCreateView.as_view()),
    path('createaccount/',views.createaccount, name='createaccount'),
    path('login/', auth_views.LoginView.as_view(template_name = 'demoapp/login.html'), name='login'),
    #path('login/',views.login,name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'demoapp/logout.html'), name='logout'),
    path('profile_post/', views.profile_post, name='profile_post'),
    path('news/', views.news, name='news'),

]
