from django.db import models

# Create your models here.
class Myblog(models.Model):
    title = models.CharField(max_length=100)
    slug= models.SlugField(max_length=150,blank=True,null=True)
    des = models.TextField()
    def __str__(self):
        return self.title