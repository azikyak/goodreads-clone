# Generated by Django 4.2.2 on 2023-06-24 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='def_pic.jpeg', upload_to=''),
        ),
    ]