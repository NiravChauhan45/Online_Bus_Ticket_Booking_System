# Generated by Django 5.0.2 on 2024-04-13 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_delete_abouts'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutt_title', models.CharField(max_length=100)),
                ('aboutt_des', models.TextField()),
            ],
        ),
    ]
