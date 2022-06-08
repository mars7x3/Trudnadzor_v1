# Generated by Django 4.0.4 on 2022-06-01 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_alter_category_options_alter_history_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='management',
            options={'ordering': ['id'], 'verbose_name': 'Руководство', 'verbose_name_plural': 'Руководство'},
        ),
        migrations.AddField(
            model_name='management',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='management',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Уроженец'),
        ),
        migrations.AddField(
            model_name='management',
            name='date',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AddField(
            model_name='management',
            name='family',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Семейное положение'),
        ),
        migrations.AddField(
            model_name='management',
            name='national',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Национальность'),
        ),
        migrations.AlterField(
            model_name='management',
            name='position',
            field=models.CharField(max_length=200, verbose_name='Должность'),
        ),
        migrations.CreateModel(
            name='Exp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Опыт работы')),
                ('management', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.management', verbose_name='Руководство')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Образование')),
                ('management', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.management', verbose_name='Руководство')),
            ],
        ),
    ]