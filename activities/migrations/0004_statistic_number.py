# Generated by Django 4.0.5 on 2022-07-18 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_statisticnumber_alter_statistic_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='number',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='activities.statisticnumber', verbose_name='ID'),
            preserve_default=False,
        ),
    ]
