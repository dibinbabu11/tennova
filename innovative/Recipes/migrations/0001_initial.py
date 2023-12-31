# Generated by Django 4.2.5 on 2023-09-29 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('prep_time', models.IntegerField()),
                ('Image', models.ImageField(blank=True, upload_to='product')),
                ('difficulty', models.CharField(max_length=500)),
                ('vegetarian', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'recipie',
                'verbose_name_plural': 'recipies',
                'ordering': ('name',),
            },
        ),
    ]
