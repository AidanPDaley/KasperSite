# Generated by Django 4.1.4 on 2022-12-12 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KasperPhotosSite', '0002_appointment_rename_photos_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='info',
            field=models.TextField(max_length=1000, verbose_name='Describe Your Photoshoot'),
        ),
    ]