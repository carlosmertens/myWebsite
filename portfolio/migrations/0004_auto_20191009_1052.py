# Generated by Django 2.2.1 on 2019-10-09 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20191007_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='title',
            field=models.CharField(default='Title', max_length=100),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=models.TextField(max_length=350),
        ),
    ]
