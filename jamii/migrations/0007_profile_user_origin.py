# Generated by Django 3.2.6 on 2021-08-27 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamii', '0006_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='User_origin',
            field=models.TextField(blank=True, choices=[('RSA', 'RSA'), ('Angola', 'Angola')], max_length=500),
        ),
    ]
