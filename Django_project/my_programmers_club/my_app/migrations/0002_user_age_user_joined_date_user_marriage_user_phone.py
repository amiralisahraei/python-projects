# Generated by Django 4.2.9 on 2024-01-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='marriage',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
