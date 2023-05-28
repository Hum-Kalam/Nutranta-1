# Generated by Django 4.2.1 on 2023-05-28 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutranta_app', '0007_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default=2, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='mobile',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
