# Generated by Django 2.2.11 on 2021-03-21 19:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_author',
            field=models.BooleanField(default=False, verbose_name='نویسنده'),
        ),
        migrations.AddField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='کاربر ویژه تا'),
        ),
    ]
