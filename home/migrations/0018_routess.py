# Generated by Django 5.0.2 on 2024-04-13 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_book_des'),
    ]

    operations = [
        migrations.CreateModel(
            name='routess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sdate', models.DateField()),
                ('edate', models.DateField()),
                ('route_name', models.CharField(max_length=100)),
                ('route_rs', models.IntegerField()),
                ('route_rating', models.CharField(max_length=100)),
            ],
        ),
    ]
