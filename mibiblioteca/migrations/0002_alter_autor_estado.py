# Generated by Django 4.2.16 on 2024-10-20 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mibiblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='estado',
            field=models.IntegerField(verbose_name='estado'),
        ),
    ]
