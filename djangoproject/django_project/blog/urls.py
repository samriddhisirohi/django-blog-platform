from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name= 'blog-home'),
   path('about/', views.about, name= 'blog-about'),
]   
#empty path means the home page of the blog app, and it will call the home function in views.py when accessed.