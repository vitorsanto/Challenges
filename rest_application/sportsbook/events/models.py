from django.db import models


class EventsModel(models.Model):
    EVENT_TYPES = (('preplay', 'Preplay'), ('inplay', 'Inplay'))
    EVENT_STATUS = (('pending', 'Pending'), ('started', 'Started'), ('ended', 'Ended'), ('cancelled', 'Cancelled'))

    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    active = models.BooleanField()
    type = models.CharField(choices=EVENT_TYPES, max_length=100)
    sport = models.ForeignKey('sports.SportsModel', on_delete=models.CASCADE)
    status = models.CharField(choices=EVENT_STATUS, max_length=100)
    scheduled_start = models.DateTimeField()
    actual_start = models.DateTimeField(null=True)

    class Meta:
        db_table = 'events'
