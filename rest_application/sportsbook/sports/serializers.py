from django.utils.text import slugify
from rest_framework import serializers


class CreateSportsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    slug = serializers.SerializerMethodField(read_only=True)
    active = serializers.BooleanField()

    def get_slug(self, instance):
        return slugify(instance['name'])


class UpdateSportsSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=100, allow_blank=True)
    slug = serializers.SerializerMethodField(read_only=True)
    active = serializers.BooleanField(allow_null=True)

    def get_slug(self, instance):
        return slugify(instance.get('name', ''))


class ListChildSportSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    slug = serializers.CharField()
    active = serializers.BooleanField()


class ListSportsSerializer(serializers.Serializer):
    sports = serializers.ListField(
        allow_empty=True,
        child=ListChildSportSerializer()
    )
