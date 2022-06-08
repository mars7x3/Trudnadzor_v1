# Generated by Django 4.0.5 on 2022-06-05 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0006_mail2_alter_categorycontact_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorycontact',
            options={'ordering': ['id'], 'verbose_name': 'Название службы', 'verbose_name_plural': 'Название службы'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['id'], 'verbose_name': 'Контакты', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AddField(
            model_name='partner',
            name='link',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Ссылка на сайт'),
        ),
    ]
