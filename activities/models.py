from django.db import models


class Question(models.Model):
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
        return f'{self.id}. {self.title}'

    class Meta:
        ordering = ['-id', ]
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


class StatisticCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='Срок отчета')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id', ]
        verbose_name_plural = 'Категория статистики'
        verbose_name = 'Категория статистики'


class StatisticNumber(models.Model):
    title = models.CharField(max_length=10, verbose_name='ID')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id', ]
        verbose_name_plural = 'Статистика ID'
        verbose_name = 'Статистика ID'


class Statistic(models.Model):
    number = models.ForeignKey(StatisticNumber, on_delete=models.DO_NOTHING, verbose_name='ID')
    title = models.CharField(max_length=300, verbose_name='Название мероприятия')
    score1 = models.CharField(max_length=100, verbose_name='Отчет до')
    score2 = models.CharField(max_length=100, verbose_name='Отчет после')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id', ]
        verbose_name_plural = 'Статистика'
        verbose_name = 'Статистика'
