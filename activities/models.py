from django.db import models


class FAQ(models.Model):
    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-id', ]
        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопрос'


class Gallery(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название фото')
    image = models.ImageField(upload_to='gallery', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id', ]
        verbose_name_plural = 'Галерея'
        verbose_name = 'Галерея'


class Link(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    link = models.TextField(verbose_name='Ссылка')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id', ]
        verbose_name_plural = 'Ссылки'
        verbose_name = 'Ссылки'

