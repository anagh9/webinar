# Generated by Django 5.0.6 on 2024-05-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='file_path',
            field=models.FileField(upload_to='static/resources/'),
        ),
    ]
