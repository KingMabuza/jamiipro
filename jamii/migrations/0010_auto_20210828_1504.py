# Generated by Django 3.2.6 on 2021-08-28 13:04

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jamii', '0009_auto_20210828_0319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', ckeditor.fields.RichTextField(null=True)),
                ('location', models.CharField(max_length=255)),
                ('booking_url', models.URLField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Importer',
        ),
        migrations.AlterField(
            model_name='exporter',
            name='Export_From',
            field=models.TextField(blank=True, choices=[('South Africa', 'South Africa'), ('Angola', 'Angola'), ('Botswana', 'Botswana'), ('Eswatini', 'Eswatini'), ('Mozambique', 'Mozambique')], max_length=500),
        ),
        migrations.AlterField(
            model_name='exporter',
            name='Export_To',
            field=models.TextField(blank=True, choices=[('South Africa', 'South Africa'), ('Angola', 'Angola'), ('Botswana', 'Botswana'), ('Eswatini', 'Eswatini'), ('Mozambique', 'Mozambique')], max_length=500),
        ),
    ]
