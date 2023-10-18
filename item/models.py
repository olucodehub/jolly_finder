from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

#  If you don't explicitly set the attribute verbose_name_plural on a Model , Django adds 's' to the name of the model when displaying .

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name