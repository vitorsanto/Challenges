from rest_framework import serializers

from selections.models import SelectionsModel


class CreateSelectionsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    event_id = serializers.IntegerField(required=True)
    price = serializers.FloatField(required=True)
    active = serializers.BooleanField()
    outcome = serializers.ChoiceField(choices=SelectionsModel.OUTCOME, required=True)


class UpdateSelectionsSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, allow_blank=True)
    event_id = serializers.IntegerField(allow_null=True)
    price = serializers.FloatField(allow_null=True)
    active = serializers.BooleanField(allow_null=True)
    outcome = serializers.ChoiceField(choices=SelectionsModel.OUTCOME, allow_blank=True)


class ListChildSportSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    event_id = serializers.IntegerField()
    price = serializers.FloatField()
    active = serializers.BooleanField()
    outcome = serializers.CharField()


class ListSelectionsSerializer(serializers.Serializer):
    sports = serializers.ListField(
        allow_empty=True,
        child=ListChildSportSerializer()
    )
