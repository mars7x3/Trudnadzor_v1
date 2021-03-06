# Generated by Django 4.0.5 on 2022-06-05 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0011_alter_management_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_ky',
            field=models.CharField(max_length=250, null=True, verbose_name='Структура'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Структура'),
        ),
        migrations.AddField(
            model_name='education',
            name='education_ky',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Образование'),
        ),
        migrations.AddField(
            model_name='education',
            name='education_ru',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Образование'),
        ),
        migrations.AddField(
            model_name='exp',
            name='exp_ky',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Опыт работы'),
        ),
        migrations.AddField(
            model_name='exp',
            name='exp_ru',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Опыт работы'),
        ),
        migrations.AddField(
            model_name='management',
            name='city_ky',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Уроженец'),
        ),
        migrations.AddField(
            model_name='management',
            name='city_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Уроженец'),
        ),
        migrations.AddField(
            model_name='management',
            name='date_ky',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AddField(
            model_name='management',
            name='date_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AddField(
            model_name='management',
            name='family_ky',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Семейное положение'),
        ),
        migrations.AddField(
            model_name='management',
            name='family_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Семейное положение'),
        ),
        migrations.AddField(
            model_name='management',
            name='position_ky',
            field=models.CharField(max_length=200, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='management',
            name='position_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='structure',
            name='name_ky',
            field=models.CharField(max_length=300, null=True, verbose_name='Имя и должность'),
        ),
        migrations.AddField(
            model_name='structure',
            name='name_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Имя и должность'),
        ),
    ]
