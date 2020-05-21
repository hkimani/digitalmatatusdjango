# Generated by Django 3.0.6 on 2020-05-21 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('agency_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('agency_name', models.CharField(max_length=100)),
                ('agency_url', models.SlugField()),
                ('agency_timezone', models.CharField(max_length=100)),
                ('agency_lang', models.CharField(max_length=10)),
                ('agency_phone', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'agency',
            },
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('service_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('monday', models.IntegerField()),
                ('tuesday', models.IntegerField()),
                ('wednesday', models.IntegerField()),
                ('thursday', models.IntegerField()),
                ('friday', models.IntegerField()),
                ('saturday', models.IntegerField()),
                ('sunday', models.IntegerField()),
                ('start_date', models.CharField(max_length=50)),
                ('end_date', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'calendar',
            },
        ),
        migrations.CreateModel(
            name='FeedInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_publisher_name', models.CharField(max_length=100)),
                ('feed_publisher_url', models.CharField(max_length=100)),
                ('feed_lang', models.CharField(max_length=100)),
                ('feed_start_date', models.CharField(max_length=100)),
                ('feed_end_date', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'feed_info',
            },
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('route_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('route_short_name', models.CharField(max_length=100)),
                ('route_long_name', models.TextField()),
                ('route_type', models.IntegerField()),
                ('agency_id', models.ForeignKey(db_column='agency_id', on_delete=django.db.models.deletion.CASCADE, to='api.Agency')),
            ],
            options={
                'db_table': 'routes',
            },
        ),
        migrations.CreateModel(
            name='Shapes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape_id', models.CharField(max_length=100)),
                ('shape_pt_lat', models.CharField(max_length=100)),
                ('shape_pt_lon', models.CharField(max_length=100)),
                ('shape_pt_sequence', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'shapes',
            },
        ),
        migrations.CreateModel(
            name='Stops',
            fields=[
                ('stop_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('stop_name', models.CharField(max_length=100)),
                ('stop_lat', models.TextField()),
                ('stop_lon', models.TextField()),
                ('location_type', models.CharField(blank=True, max_length=10, null=True)),
                ('parent_station', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'stops',
            },
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('trip_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('trip_headsign', models.CharField(max_length=100)),
                ('direction_id', models.CharField(max_length=100)),
                ('shape_id', models.CharField(max_length=100)),
                ('route_id', models.ForeignKey(db_column='route_id', on_delete=django.db.models.deletion.CASCADE, to='api.Routes')),
                ('service_id', models.ForeignKey(db_column='service_id', on_delete=django.db.models.deletion.CASCADE, to='api.Calendar')),
            ],
            options={
                'db_table': 'trips',
            },
        ),
        migrations.CreateModel(
            name='StopTimes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_time', models.CharField(max_length=100)),
                ('departure_time', models.CharField(max_length=100)),
                ('stop_sequence', models.CharField(max_length=100)),
                ('stop_id', models.ForeignKey(db_column='stop_id', on_delete=django.db.models.deletion.CASCADE, to='api.Stops')),
                ('trip_id', models.ForeignKey(db_column='trip_id', on_delete=django.db.models.deletion.CASCADE, to='api.Trips')),
            ],
            options={
                'db_table': 'stop_times',
            },
        ),
        migrations.CreateModel(
            name='Frequencies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=100)),
                ('end_time', models.CharField(max_length=100)),
                ('headway_secs', models.IntegerField()),
                ('trip_id', models.ForeignKey(db_column='trip_id', on_delete=django.db.models.deletion.CASCADE, to='api.Trips')),
            ],
            options={
                'db_table': 'frequencies',
            },
        ),
        migrations.CreateModel(
            name='CalendarDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('exception_type', models.IntegerField()),
                ('service_id', models.ForeignKey(db_column='service_id', on_delete=django.db.models.deletion.CASCADE, to='api.Calendar')),
            ],
            options={
                'db_table': 'calendar_dates',
            },
        ),
    ]
