# Generated by Django 2.1 on 2019-03-04 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skate', '0005_auto_20190304_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='spot_images'),
        ),
    ]
