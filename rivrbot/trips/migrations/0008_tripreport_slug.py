# Generated by Django 2.1.2 on 2018-11-22 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0007_auto_20181114_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripreport',
            name='slug',
            field=models.SlugField(blank=True, max_length=12, unique=True),
        ),
    ]
