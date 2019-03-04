# Generated by Django 2.1 on 2019-03-03 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot_name', models.CharField(max_length=200)),
                ('spot_address', models.CharField(max_length=400)),
                ('spot_description', models.CharField(max_length=800)),
                ('picture', models.ImageField(default='default.jpg', upload_to='media/Images/')),
            ],
        ),
    ]
