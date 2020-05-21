from django.db import models
import datetime

# Create your models here.
class Agency(models.Model):
    agency_id = models.CharField(max_length=100, primary_key=True)
    agency_name = models.CharField(max_length=100)
    agency_url = models.SlugField()
    agency_timezone = models.CharField(max_length=100)
    agency_lang = models.CharField(max_length=10)
    agency_phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'agency'

class Calendar(models.Model):
    service_id = models.CharField(max_length=100, primary_key=True)
    monday = models.IntegerField()
    tuesday = models.IntegerField()
    wednesday = models.IntegerField()
    thursday = models.IntegerField()
    friday = models.IntegerField()
    saturday = models.IntegerField()
    sunday = models.IntegerField()
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)

    class Meta:
        db_table = 'calendar'

class CalendarDates(models.Model):
    service_id = models.ForeignKey(Calendar, on_delete=models.CASCADE, db_column='service_id')
    date = models.CharField(max_length=100)
    exception_type = models.IntegerField()

    class Meta:
        db_table = 'calendar_dates'

class FeedInfo(models.Model):
    feed_publisher_name = models.CharField(max_length=100)
    feed_publisher_url = models.CharField(max_length=100)
    feed_lang = models.CharField(max_length=100)
    feed_start_date = models.CharField(max_length=100)
    feed_end_date = models.CharField(max_length=100)

    class Meta:
        db_table = 'feed_info'

class Shapes(models.Model):
    shape_id = models.CharField(max_length=100)
    shape_pt_lat = models.CharField(max_length=100)
    shape_pt_lon = models.CharField(max_length=100)
    shape_pt_sequence = models.CharField(max_length=100)

    class Meta:
        db_table = 'shapes'

class Routes(models.Model):
    route_id = models.CharField(max_length=100, primary_key=True)
    agency_id = models.ForeignKey(Agency, on_delete=models.CASCADE, db_column='agency_id')
    route_short_name = models.CharField(max_length=100)
    route_long_name = models.TextField()
    route_type = models.IntegerField()

    class Meta:
        db_table = 'routes'

class Stops(models.Model):
    stop_id = models.CharField(max_length=100, primary_key=True)
    stop_name = models.CharField(max_length=100)
    stop_lat = models.TextField()
    stop_lon = models.TextField()
    location_type = models.CharField(max_length=10, blank=True, null=True)
    parent_station = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'stops'

class Trips(models.Model):
    trip_id = models.CharField(max_length=100, primary_key=True)
    route_id = models.ForeignKey(Routes, on_delete=models.CASCADE, db_column='route_id')
    service_id = models.ForeignKey(Calendar, on_delete=models.CASCADE, db_column='service_id')
    trip_headsign = models.CharField(max_length=100)
    direction_id = models.CharField(max_length=100)
    shape_id = models.CharField(max_length=100)

    class Meta:
        db_table = 'trips'

class StopTimes(models.Model):
    trip_id = models.ForeignKey(Trips, on_delete=models.CASCADE, db_column='trip_id')
    arrival_time = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    stop_id = models.ForeignKey(Stops, on_delete=models.CASCADE, db_column='stop_id')
    stop_sequence = models.CharField(max_length=100)

    class Meta:
        db_table = 'stop_times'

class Frequencies(models.Model):
    trip_id = models.ForeignKey(Trips, on_delete=models.CASCADE, db_column='trip_id')
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    headway_secs = models.IntegerField()

    class Meta:
        db_table = 'frequencies'