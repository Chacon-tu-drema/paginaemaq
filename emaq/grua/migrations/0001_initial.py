# Generated by Django 2.1.5 on 2020-04-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre Grua')),
                ('content', models.TextField(verbose_name='Descripcion')),
                ('maxalto', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Alto Maximo')),
                ('maxlargo', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Largo Maximo')),
                ('maxcarga', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Carga Maximo')),
                ('image', models.ImageField(upload_to='grua/grua/imagen', verbose_name='Imagen')),
                ('doc', models.FileField(upload_to='grua/grua/ficha', verbose_name='Ficha Tecnica')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'grua',
                'verbose_name_plural': 'gruas',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=100, unique=True, verbose_name='Nombre Serie')),
                ('image', models.ImageField(upload_to='grua/serie', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'serie',
                'verbose_name_plural': 'series',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='grua',
            name='serie',
            field=models.ManyToManyField(related_name='get_grua', to='grua.Serie', verbose_name='Series'),
        ),
    ]