# Generated by Django 4.0.4 on 2022-05-30 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0004_mail1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail1',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='email_files', verbose_name='Файл'),
        ),
    ]