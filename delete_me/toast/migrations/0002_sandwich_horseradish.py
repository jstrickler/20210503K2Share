# Generated by Django 3.0 on 2021-05-05 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sandwich',
            name='horseradish',
            field=models.BooleanField(default=False),
        ),
    ]
