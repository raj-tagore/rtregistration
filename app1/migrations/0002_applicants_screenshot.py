# Generated by Django 2.2.7 on 2020-04-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicants',
            name='screenshot',
            field=models.ImageField(default='null', upload_to=''),
        ),
    ]
