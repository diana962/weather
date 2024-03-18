from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30,
                            unique=True)
    class Meta:
        verbose_name_plural = 'Города'
        verbose_name = 'Город'

    def __str__(self):
       return f'{self.name}'