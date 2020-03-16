
from django.urls import path
from .views import News,Home,Contact

urlpatterns = [
    path('home/',Home ,name='Home'),
    path('news/',News ,name='News'),
    path('contact/',Contact ,name='Contact'),
]