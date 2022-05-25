# Generated by Django 3.2.5 on 2022-05-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20220512_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='FemalePants',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('weight', models.IntegerField()),
                ('age', models.IntegerField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('size', models.CharField(max_length=5)),
                ('gender', models.CharField(max_length=5)),
                ('tummy_shape', models.CharField(max_length=20)),
                ('fit_preference', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('waist', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FemaleShirts',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('weight', models.IntegerField()),
                ('age', models.IntegerField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('size', models.CharField(max_length=5)),
                ('gender', models.CharField(max_length=5)),
                ('tummy_shape', models.CharField(max_length=20)),
                ('fit_preference', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('chest', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MalePants',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('weight', models.IntegerField()),
                ('age', models.IntegerField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('size', models.CharField(max_length=5)),
                ('gender', models.CharField(max_length=5)),
                ('tummy_shape', models.CharField(max_length=20)),
                ('fit_preference', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('waist', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MaleShirts',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('weight', models.IntegerField()),
                ('age', models.IntegerField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('size', models.CharField(max_length=5)),
                ('gender', models.CharField(max_length=5)),
                ('tummy_shape', models.CharField(max_length=20)),
                ('fit_preference', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('chest', models.IntegerField()),
            ],
        ),
    ]