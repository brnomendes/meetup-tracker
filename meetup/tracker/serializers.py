from rest_framework import serializers

from tracker.models import Location


class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for Location Model.
    """

    class Meta:
        model = Location
        fields = "__all__"
