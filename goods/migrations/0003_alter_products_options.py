# Generated by Django 4.2.15 on 2024-09-10 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_categories_options_alter_categories_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]