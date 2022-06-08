from django.db import models


class News(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    announcement = models.CharField(max_length=200, null=True, blank=True, verbose_name='Анонс')
    image = models.ImageField(upload_to='news_images', verbose_name='Фото')
    video = models.CharField(max_length=500, verbose_name='Ссылка на видео', blank=True, null=True, default='#')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id', ]
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'

