# Generated by Django 5.0.2 on 2024-04-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_payment_paid'),
    ]

    operations = [
        migrations.CreateModel(
            name='routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('des', models.TextField()),
            ],
        ),
    ]
