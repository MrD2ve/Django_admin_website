# Generated by Django 4.0.6 on 2022-07-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
