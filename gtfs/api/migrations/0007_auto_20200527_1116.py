# Generated by Django 3.0.6 on 2020-05-27 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_fares_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fares',
            name='period',
            field=models.CharField(default='11:00-1:00', max_length=100),
        ),
    ]
