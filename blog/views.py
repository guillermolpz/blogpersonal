from django.shortcuts import render, HttpResponse
from .models import Blog
# Create your views here.
def posts(request):
    first_blog = Blog.objects.first()
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs':blogs, 'first_blog':first_blog})

def post(request, id):
    blog = Blog.objects.get(id=id)
    #contenido = f'Titulo: {blogs.titulo} Descripcion: {blogs.descripcion}'
    #return HttpResponse(contenido)
    return render(request, 'blog.html', {'blog':blog})