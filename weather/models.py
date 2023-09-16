from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50,null=True)

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name_plural="cities"

# Create your models here.
