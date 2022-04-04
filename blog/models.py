from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

#CKEDITOR
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    imagen = models.ImageField(verbose_name='Imagen', upload_to='blog') 
    titulo = models.CharField(max_length=200, verbose_name='Titulo')
    descripcion = models.TextField(verbose_name='Descripcion')
    contenido = RichTextField(verbose_name='Contenido')
    
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    
    class Meta:
        verbose_name= 'Publicación'
        verbose_name_plural= 'Publicaciones'
        ordering = ['-created']
    
    def __str__(self):
        return self.titulo