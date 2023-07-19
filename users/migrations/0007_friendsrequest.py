# Generated by Django 4.2.2 on 2023-07-14 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_friends_options_friends_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendsRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, verbose_name='Message')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('viewed', models.DateTimeField(blank=True, null=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Friend Request',
                'verbose_name_plural': 'Friend Requests',
                'unique_together': {('from_user', 'to_user')},
            },
        ),
    ]