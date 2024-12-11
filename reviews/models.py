from django.db import models

class Review(models.Model):
    author_name = models.CharField(max_length=100, verbose_name="Автор")
    author_info = models.CharField(max_length=255, blank=True, null=True, verbose_name="Информация об авторе")
    text = models.TextField(verbose_name="Текст отзыва")
    rating = models.PositiveSmallIntegerField(verbose_name="Рейтинг")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    
    def __str__(self):
        return f"{self.author_name} - {self.rating}/5"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']
