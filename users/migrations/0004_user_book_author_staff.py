# Generated by Django 4.2.2 on 2023-07-05 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_city_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='book_author_staff',
            field=models.BooleanField(default=False),
        ),
    ]
