# Generated by Django 4.2.9 on 2024-01-22 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_user_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]