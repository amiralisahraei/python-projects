# Generated by Django 4.2.9 on 2024-01-23 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_alter_user_marriage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='marriage',
            new_name='married',
        ),
    ]
