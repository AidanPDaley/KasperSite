# Generated by Django 4.1.4 on 2022-12-12 22:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KasperPhotosSite', '0007_alter_blog_createdat_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 22, 40, 1, 506395, tzinfo=datetime.timezone.utc)),
        ),
    ]