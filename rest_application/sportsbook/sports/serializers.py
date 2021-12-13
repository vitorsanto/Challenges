from django.utils.text import slugify
from rest_framework import serializers


class SportsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    slug = serializers.SerializerMethodField(read_only=True)
    active = serializers.BooleanField(default=True)

    def get_slug(self, instance):
        print(instance)
        return slugify(instance['name'])
