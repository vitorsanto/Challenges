from django.db import models


class SportsModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    active = models.BooleanField()

    class Meta:
        db_table = 'sports'
