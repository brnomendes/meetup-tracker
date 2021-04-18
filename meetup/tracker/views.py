from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.response import Response

from tracker.integration.client_api import UpdateMeetupGroup
from tracker.models import Location, MeetupGroup
from tracker.serializers import LocationSerializer, MeetupEventSerializer, MeetupGroupSerializer


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


class MeetupEventList(generics.ListAPIView):
    """
    View that list MeetupEvent models by group id.
    """

    serializer_class = MeetupEventSerializer

    def get(self, request, pk, *args, **kwargs):
        try:
            group = MeetupGroup.objects.get(pk=pk)
            serialized = self.serializer_class(group.events, many=True)
            return Response(serialized.data, status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response("", status.HTTP_404_NOT_FOUND)


class MeetupUpdate(generics.ListAPIView):
    """"""

    def get(self, request, pk, *args, **kwargs):
        try:
            group = MeetupGroup.objects.get(pk=pk)
            update = UpdateMeetupGroup(group.urlname)
            update.update_group()
            return Response("", status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response("", status.HTTP_404_NOT_FOUND)
