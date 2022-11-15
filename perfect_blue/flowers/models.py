from django.db import models
from django.urls import reverse


class Flowers(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.CharField(max_length=10, verbose_name='Цена')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    cat = models.ForeignKey('Categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цветы'
        verbose_name_plural = 'Цветы'
        ordering = ['title', 'price']


class Categories(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'flower_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
