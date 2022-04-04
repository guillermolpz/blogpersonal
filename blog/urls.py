from django.urls import path

#Views
from . import views

#Config URL
urlpatterns = [
    path('', views.posts, name='Publicaciones'),
    path('<int:id>', views.post, name='Blog'),
]