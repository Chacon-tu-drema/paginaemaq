# Generated by Django 2.1.5 on 2020-04-13 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grua', '0003_auto_20200413_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grua',
            name='category',
            field=models.ManyToManyField(to='grua.Serie', verbose_name='Series'),
        ),
    ]
