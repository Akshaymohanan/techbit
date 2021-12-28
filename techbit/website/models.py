from django.db import models

# Create your models here.

class Projects(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/products', blank=True, default='image')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('name',)
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __str__(self):
        return '{}'.format(self.name)
