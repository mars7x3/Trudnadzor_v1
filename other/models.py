from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=200, verbose_name='Партнер')
    logo = models.ImageField(upload_to='partners_logo', verbose_name='Логотип')
    link = models.CharField(max_length=300, blank=True, null=True, verbose_name='Ссылка на сайт')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id', ]
        verbose_name_plural = 'Партнеры'
        verbose_name = 'Партнеры'


class CategoryContact(models.Model):
    department = models.CharField(max_length=300, verbose_name='Название службы')

    def __str__(self):
        return self.department

    class Meta:
        ordering = ['id', ]
        verbose_name_plural = 'Название службы'
        verbose_name = 'Название службы'


class Contact(models.Model):
    department = models.ForeignKey(CategoryContact, on_delete=models.CASCADE, verbose_name='Название службы')
    title = models.CharField(max_length=300, verbose_name='Должность')
    address = models.CharField(max_length=300, verbose_name='Адрес')

    def __str__(self):
        return f'{self.department} --- {self.title}'

    class Meta:
        ordering = ['id', ]
        verbose_name_plural = 'Контакты'
        verbose_name = 'Контакты'


class PhoneContact(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='Контакты')
    phone = models.CharField(max_length=100, verbose_name='Телефон')


class Mail1(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Фамилия')
    name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отчество')
    email = models.CharField(max_length=100, verbose_name='Почта')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    text = models.TextField(verbose_name='Текст')
    file = models.FileField(upload_to='email_files', blank=True, null=True, verbose_name='Файл')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.name} {self.file}'

    class Meta:
        ordering = ['-id', ]
        verbose_name_plural = 'Обращения Физ лица'
        verbose_name = 'Обращение Физ лицо'


class Mail2(models.Model):
    organ = models.CharField(max_length=100, verbose_name='Наименование организации')
    inn = models.CharField(max_length=100, verbose_name='ИНН')
    position = models.CharField(max_length=100, verbose_name='Должность')
    first_name = models.CharField(max_length=100, verbose_name='Фамилия')
    name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отчество')
    email = models.CharField(max_length=100, verbose_name='Почта')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    text = models.TextField(verbose_name='Текст')
    file = models.FileField(upload_to='email_files', blank=True, null=True, verbose_name='Файл')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id', ]
        verbose_name_plural = 'Обращения Юр лица'
        verbose_name = 'Обращение Юр лицо'

#
# class Job(models.Model):
#