from django.db import models


class Management(models.Model):
    name = models.CharField(max_length=200, verbose_name='Ф.И.О')
    image = models.ImageField(upload_to='Management_image', verbose_name='Фото')
    position = models.CharField(max_length=200, verbose_name='Должность')
    date = models.CharField(max_length=100, blank=True, null=True, verbose_name='Дата рождения')
    city = models.CharField(max_length=200, blank=True, null=True, verbose_name='Уроженец')
    national = models.CharField(max_length=100, null=True, blank=True, verbose_name='Национальность')
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='Телефон')
    family = models.CharField(max_length=200, blank=True, null=True, verbose_name='Семейное положение')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id', ]
        verbose_name_plural = 'Руководство'
        verbose_name = 'Руководство'


class Education(models.Model):
    management = models.ForeignKey(Management, on_delete=models.CASCADE, verbose_name='Руководство')
    education = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Образование')


class Exp(models.Model):
    management = models.ForeignKey(Management, on_delete=models.CASCADE, verbose_name='Руководство')
    exp = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Опыт работы')


class History(models.Model):
    history = models.TextField()

    def __str__(self):
        return 'История'

    class Meta:
        ordering = ['id', ]
        verbose_name_plural = 'История'
        verbose_name = 'История'


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name='Структура')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id', ]
        verbose_name_plural = 'Структура'
        verbose_name = 'Структура'


class Structure(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Отдел', related_name='structures')
    name = models.CharField(max_length=300, verbose_name='Имя и должность')

    def __str__(self):
        return f'{self.category} --- {self.name}'

    class Meta:
        ordering = ['id', ]
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудники'

