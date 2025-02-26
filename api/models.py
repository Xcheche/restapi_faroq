from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering = ['date']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'