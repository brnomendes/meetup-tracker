from rest_framework import serializers

from tracker.models import GroupUrlname, Location


class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for Location Model.
    """

    class Meta:
        model = Location
        fields = "__all__"


class GroupUrlnameSerializer(serializers.ModelSerializer):
    """
    Serializer for GroupUrlname Model.
    """

    class Meta:
        model = GroupUrlname
        fields = "__all__"
