# Generated by Django 2.0.5 on 2020-04-13 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grua', '0005_auto_20200413_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grua',
            name='categories',
            field=models.ManyToManyField(related_name='get_grua', to='grua.Serie', verbose_name='Series'),
        ),
    ]
