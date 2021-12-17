from datetime import datetime

import factory


class SportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'sports.SportsModel'  # Equivalent to ``model = myapp.models.User``

    name = 'Soccer'
    active = True


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'events.EventsModel'

    active = True
    scheduled_start = datetime.now()
