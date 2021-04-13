from rest_framework import generics

from tracker.models import Location, MeetupGroup
from tracker.serializers import LocationSerializer, MeetupGroupSerializer


class LocationList(generics.ListAPIView):
    """
    View that list Location models.
    """

    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class MeetupGroupList(generics.ListAPIView):
    """
    View that list MeetupGroup models.
    """

    queryset = MeetupGroup.objects.all()
    serializer_class = MeetupGroupSerializer
