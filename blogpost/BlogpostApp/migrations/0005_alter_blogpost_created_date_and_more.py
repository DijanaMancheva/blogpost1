# Generated by Django 4.0.4 on 2022-05-31 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogpostApp', '0004_remove_blogpost_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]