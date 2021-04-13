from conftest import location
from rest_framework import serializers

from tracker.models import City, Country, GroupUrlname, Location, MeetupEvent, MeetupGroup


class CountrySerializer(serializers.ModelSerializer):
    """
    Serializer for Country Model.
    """

    class Meta:
        model = Country
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    """
    Serializer for City Model.
    """

    country = CountrySerializer()

    class Meta:
        model = City
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for Location Model.
    """

    city = CitySerializer()

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

    location = LocationSerializer()

    class Meta:
        model = MeetupEvent
        fields = "__all__"
