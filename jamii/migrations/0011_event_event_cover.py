# Generated by Django 3.2.6 on 2021-08-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamii', '0010_auto_20210828_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_cover',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
