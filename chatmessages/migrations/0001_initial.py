# Generated by Django 3.2 on 2022-08-21 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatmessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('formuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentmessage', to=settings.AUTH_USER_MODEL)),
                ('touser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indoxmessage', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
