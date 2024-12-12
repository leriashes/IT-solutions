from django.db import models

class Review(models.Model):
    author_name = models.CharField(max_length=100, verbose_name="Автор")
    author_photo = models.CharField(max_length=255, blank=True, null=True, verbose_name="Аватар")
    text = models.TextField(verbose_name="Текст отзыва")
    rating = models.PositiveSmallIntegerField(verbose_name="Рейтинг")
    date_created = models.DateTimeField(verbose_name="Дата создания")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.author_name} - {self.rating}/5"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-date_created']
