# Generated by Django 2.1 on 2019-03-03 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skate', '0005_remove_spot_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='picture',
            field=models.ImageField(upload_to='media/Images/'),
        ),
    ]
