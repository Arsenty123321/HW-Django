from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя_категории')
    description = models.TextField(verbose_name='Описание_категории')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя_продукта')
    description = models.TextField(verbose_name='Описание_продукта')
    image = models.ImageField(upload_to='product_images/', verbose_name='Изображение_продукта', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    price = models.IntegerField(verbose_name='Цена_продукта')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    STATUS_CHOICES = [
        ('unpublished', 'Не опубликован'),
        ('published', 'Опубликован'),
    ]

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='unpublished',
        verbose_name='Статус публикации',
    )

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]
