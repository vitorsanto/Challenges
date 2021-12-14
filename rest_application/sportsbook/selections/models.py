from django.core.exceptions import ValidationError
from django.db import models


def validate_decimals(value):
    try:
        return round(float(value), 2)
    except:
        raise ValidationError(
            '%(value)s is not an integer or a float  number',
            params={'value': value},
        )


class SelectionsModel(models.Model):
    OUTCOME = (('unsettled', 'Unsettled'), ('void', 'Void'), ('lose', 'Lose'), ('win', 'Win'))

    name = models.CharField(max_length=100)
    active = models.BooleanField()
    price = models.FloatField(validators=[validate_decimals])
    event = models.ForeignKey('events.EventsModel', on_delete=models.CASCADE)
    outcome = models.CharField(choices=OUTCOME, max_length=100)

    class Meta:
        db_table = 'selections'
