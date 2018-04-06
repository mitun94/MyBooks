from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, default=False)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class BookItem(models.Model):
    title       = models.CharField(max_length=50, default=False)
    author      = models.CharField(max_length=20, default=False)
    category    = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField(max_length=200, default=False)

    def __str__(self):
        return self.title

