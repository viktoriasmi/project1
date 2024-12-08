from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(upload_to='news_images', verbose_name='Изображение')
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    content = models.TextField(verbose_name='Текст новости')

    class Meta:
        db_table = "news"
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title
