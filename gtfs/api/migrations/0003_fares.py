# Generated by Django 3.0.6 on 2020-05-26 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200524_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fares',
            fields=[
                ('fare_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('currency_type', models.CharField(max_length=50)),
                ('payment_method', models.IntegerField()),
                ('destination_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_stop_id', to='api.Stops')),
                ('origin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_stop_id', to='api.Stops')),
                ('route_id', models.ForeignKey(db_column='route_id', on_delete=django.db.models.deletion.CASCADE, to='api.Routes')),
            ],
            options={
                'db_table': 'fares',
            },
        ),
    ]
