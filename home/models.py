from django.db import models


class About(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название о службе')
    text = models.TextField(verbose_name='Обращение', blank=True, null=True)

    def __str__(self):
        return 'О службе на главной странице'

    class Meta:
        ordering = ['id', ]
        verbose_name_plural = 'О нас'
        verbose_name = 'О нас'


class AboutText(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_texts')
    id = models.PositiveIntegerField(unique=True, primary_key=True, verbose_name='Номер порядка')
    text = models.TextField(verbose_name='Текст')


class AboutImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_images')
    image = models.ImageField(upload_to='about-images', verbose_name='Фото')


class AboutVideo(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_videos')
    image = models.ImageField(upload_to='about-video', verbose_name='Фото на видео')
    video = models.CharField(max_length=500, verbose_name='Ссылка на видео')


class AboutTask(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_tasks')
    title = models.CharField(max_length=300, verbose_name='Название основных задач службы')


class TaskText(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_task_text')
    text = models.TextField(verbose_name='Текст')


class TaskImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='y')
    image = models.ImageField(upload_to='about-task-image', verbose_name='Фото задачи')


class Power(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_power')
    title = models.CharField(max_length=300, verbose_name='Название полномочий')


class PowerText(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_power_text')
    text = models.TextField(verbose_name='Текст')


class GosOrgan(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    link = models.CharField(max_length=200, verbose_name='Ссылка на сайт')
    image = models.ImageField(upload_to='gos-organ', verbose_name='Логотип')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id', ]
        verbose_name_plural = 'Гос органы'
        verbose_name = 'Гос органы'
