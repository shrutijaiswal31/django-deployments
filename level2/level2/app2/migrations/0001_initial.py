# Generated by Django 2.1.7 on 2019-03-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=125)),
                ('lastName', models.CharField(max_length=125)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
