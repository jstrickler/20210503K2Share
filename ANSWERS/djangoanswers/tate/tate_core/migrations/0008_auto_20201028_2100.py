# Generated by Django 3.1.2 on 2020-10-29 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tate_core', '0007_auto_20201028_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='place_of_birth',
            field=models.CharField(help_text="Location of artist's birth", max_length=256, null=True),
        ),
    ]
