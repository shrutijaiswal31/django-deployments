# Generated by Django 2.1.7 on 2019-03-11 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=125, unique=True),
        ),
    ]
