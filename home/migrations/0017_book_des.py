# Generated by Django 5.0.2 on 2024-04-13 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_delete_routes'),
    ]

    operations = [
        migrations.CreateModel(
            name='book_des',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('book_des', models.TextField()),
            ],
        ),
    ]
