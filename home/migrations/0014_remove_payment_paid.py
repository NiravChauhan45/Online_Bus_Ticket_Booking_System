# Generated by Django 5.0.2 on 2024-03-18 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rename_coffee_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='paid',
        ),
    ]