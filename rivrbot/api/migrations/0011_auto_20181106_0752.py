# Generated by Django 2.1.2 on 2018-11-06 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20181105_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='currencies',
        ),
        migrations.RemoveField(
            model_name='country',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='country',
            name='regional_blocs',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Currency',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='RegionalBloc',
        ),
    ]
