from rest_framework import generics

from tracker.models import Location
from tracker.serializers import LocationSerializer


class LocationList(generics.ListAPIView):
    """
    View that list Location models.
    """

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
