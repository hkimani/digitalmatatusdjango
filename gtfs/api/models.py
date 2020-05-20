from django.db import models

# Create your models here.
class Agency(models.Model):
    agency_id = models.CharField(max_length=100, primary_key=True)
    agency_name = models.CharField(max_length=100)
    agency_url = models.TextField(max_length=1000)
    agency_timezone = models.CharField(max_length=100)
    agency_lang = models.CharField(max_length=10)
    agency_phone = models.CharField(max_length=50)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)

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
    service_id = models.ForeignKey(Calendar, on_delete=models.CASCADE)
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
    shape_id = models.CharField(max_length=100, primary_key=True)
    shape_pt_lat = models.CharField(max_length=100)
    shape_pt_lon = models.CharField(max_length=100)
    shape_pt_sequence = models.CharField(max_length=100)

    class Meta:
        db_table = 'shapes'

class Routes(models.Model):
    route_id = models.CharField(max_length=100, primary_key=True)
    agency_id = models.ForeignKey(Agency, on_delete=models.CASCADE)
    route_short_name = models.CharField(max_length=100)
    route_long_name = models.TextField(max_length=1000)
    route_type = models.IntegerField()

    class Meta:
        db_table = 'routes'

class Stops(models.Model):
    stop_id = models.CharField(max_length=100, primary_key=True)
    stop_name = models.CharField(max_length=100)
    stop_lat = models.TextField(max_length=500)
    stop_lon = models.TextField(max_length=500)
    location_type = models.IntegerField(blank=True, null=True)
    parent_station = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'stops'

class Trips(models.Model):
    trip_id = models.CharField(max_length=100, primary_key=True)
    route_id = models.ForeignKey(Routes, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    trip_headsign = models.CharField(max_length=100)
    direction_id = models.CharField(max_length=100)
    shape_id = models.ForeignKey(Shapes, on_delete=models.CASCADE)

    class Meta:
        db_table = 'trips'

class StopTimes(models.Model):
    trip_id = models.ForeignKey(Trips, on_delete=models.CASCADE)
    arrival_time = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    stop_id = models.ForeignKey(Stops, on_delete=models.CASCADE)
    stop_sequence = models.CharField(max_length=100)

    class Meta:
        db_table = 'stop_times'

class Frequencies(models.Model):
    trip_id = models.ForeignKey(Trips, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    headway_secs = models.IntegerField()

    class Meta:
        db_table = 'frequencies'