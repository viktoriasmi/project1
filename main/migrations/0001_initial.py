# Generated by Django 4.2.15 on 2024-11-04 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('image', models.ImageField(upload_to='news_images', verbose_name='Изображение')),
                ('publication_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('content', models.TextField(verbose_name='Текст новости')),
            ],
        ),
    ]
