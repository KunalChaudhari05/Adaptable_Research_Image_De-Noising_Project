# Generated by Django 4.1.5 on 2023-05-01 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_image_denoising_denoised_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_denoising',
            name='denoised_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
