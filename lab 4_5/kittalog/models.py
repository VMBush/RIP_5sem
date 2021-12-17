from django.db import models
from django.urls import reverse
import os

# Create your models here.


def get_user_img_path(instance, filename):

    return os.path.join('images', 'kit_{}'.format(instance.type), '{}'.format(filename))


class Kit(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    picture = models.ImageField(upload_to=get_user_img_path)
    shelter = models.ForeignKey(
        'Shelter', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("kit_detail", args=[str(self.id)])


class Shelter(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='images\\shelters')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("kittalog", args=[str(self.id)])

    def get_kit_num(self):
        return Kit.objects.filter(shelter__exact=self.id).count()
