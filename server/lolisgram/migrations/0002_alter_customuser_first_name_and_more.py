# Generated by Django 4.2.7 on 2024-05-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lolisgram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
