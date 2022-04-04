from django.db import models

#CKEDITOR
from ckeditor.fields import RichTextField

# Create your models here.
class Project(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    descripcion = models.TextField(verbose_name='Descripción')
    
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name= 'Proyecto'
        verbose_name_plural= 'Proyectos'
        ordering = ['created']
        
    def __str__(self):
        return self.titulo