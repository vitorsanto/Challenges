from datetime import datetime

from django.utils.text import slugify
from rest_framework import serializers

from events.models import EventsModel


class CreateEventsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    slug = serializers.SerializerMethodField(read_only=True)
    active = serializers.BooleanField()
    type = serializers.ChoiceField(choices=EventsModel.EVENT_TYPES, required=True)
    sport_id = serializers.IntegerField(required=True)
    status = serializers.ChoiceField(choices=EventsModel.EVENT_STATUS, required=True)
    scheduled_start = serializers.DateTimeField(required=True)

    def get_slug(self, instance):
        return slugify(instance['name'])


class UpdateEventsSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, allow_blank=True)
    slug = serializers.SerializerMethodField(read_only=True)
    active = serializers.BooleanField()
    type = serializers.ChoiceField(choices=('preplay', 'inplay'), allow_blank=True)
    sport_id = serializers.IntegerField(allow_null=True)
    status = serializers.ChoiceField(choices=('Pending', 'Started', 'Ended', 'Cancelled'), allow_blank=True)
    scheduled_start = serializers.DateTimeField(allow_null=True)

    def get_slug(self, instance):
        return slugify(instance['name'])


class ListChildSportSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    slug = serializers.CharField()
    active = serializers.BooleanField()
    type = serializers.CharField()
    sport_id = serializers.IntegerField()
    status = serializers.CharField()
    scheduled_start = serializers.DateTimeField()


class ListEventsSerializer(serializers.Serializer):
    sports = serializers.ListField(
        allow_empty=True,
        child=ListChildSportSerializer()
    )
