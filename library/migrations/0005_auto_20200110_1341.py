# Generated by Django 3.0.2 on 2020-01-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default='profile_photo/photo.jpeg', upload_to='profile_photo/'),
        ),
    ]
