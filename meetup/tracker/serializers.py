from conftest import location
from rest_framework import serializers

from tracker.models import GroupUrlname, Location, MeetupEvent, MeetupGroup


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


class MeetupGroupSerializer(serializers.ModelSerializer):
    """
    Serializer for MeetupGroup Model.
    """

    location = LocationSerializer()
    urlname = GroupUrlnameSerializer()

    class Meta:
        model = MeetupGroup
        fields = "__all__"


class MeetupEventSerializer(serializers.ModelSerializer):
    """
    Serializer for MeetupEvent Model.
    """

    class Meta:
        model = MeetupEvent
        fields = "__all__"
