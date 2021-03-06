# Generated by Django 2.1.4 on 2019-01-17 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date and time published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.CharField(max_length=1000, verbose_name='Post text'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date and Time published'),
        ),
    ]
