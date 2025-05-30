from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Имя_категории')
    description = models.TextField(verbose_name='Описание_категории')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category_name']


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Имя_продукта')
    description = models.TextField(verbose_name='Описание_продукта')
    image = models.ImageField(upload_to='product_images/', verbose_name='Изображение_продукта', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    price = models.IntegerField(verbose_name='Цена_продукта')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product_name} {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['product_name', 'category', 'price']
