# Generated by Django 2.1.7 on 2019-02-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
