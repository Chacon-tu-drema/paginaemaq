# Generated by Django 2.0.5 on 2020-04-13 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['created'], 'verbose_name': 'pagina', 'verbose_name_plural': 'paginas'},
        ),
        migrations.RemoveField(
            model_name='page',
            name='order',
        ),
    ]