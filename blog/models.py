from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=60, verbose_name="Заголовок", help_text="Введите заголовок блога")
    content = models.TextField(verbose_name="Содержимое", help_text="Введите содержимое блога")
    preview = models.ImageField(upload_to="blog_images", verbose_name="Изображение",
                                help_text="Загрузите изображение блога", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовать",
                                       help_text="Отметьте для публикации")
    views_count = models.PositiveIntegerField(
        default=0, verbose_name="Просмотры", help_text="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["-created_at"]
