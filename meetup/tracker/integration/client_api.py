from threading import Thread

import requests
from django.core.exceptions import ObjectDoesNotExist
from tracker.models import Location, MeetupGroup


class UpdateMeetupGroup(Thread):
    API_URL = "https://api.meetup.com"

    def __init__(self, group_urlname):
        Thread.__init__(self)
        self._group_urlname = group_urlname

    def run(self):
        self.update()

    def update(self):
        """
        Updates the group and events model with the data from the Meetup API.
        """
        response = requests.get(f"{self.API_URL}/{self._group_urlname.urlname}")
        if response.status_code != 200:
            return
        content = response.json()
        self.update_group_data(content)

    def update_group_data(self, content):
        """
        Receive JSON from the Meetup API and create or update the group model.
        """
        try:
            group = MeetupGroup.objects.get(urlname=self._group_urlname)
        except ObjectDoesNotExist:
            group = MeetupGroup()
            group.id = self._get_attr(content, "id")
            group.urlname = self._group_urlname
            group.location = Location()

        group.name = self._get_attr(content, "name")
        group.status = self._get_attr(content, "status")
        group.link = self._get_attr(content, "link")
        group.member_count = self._get_attr(content, "members")
        group.description = self._get_attr(content, "description")
        key_photo = self._get_attr(content, "key_photo")
        if key_photo:
            group.photo_link = self._get_attr(key_photo, "photo_link")

        group.location.city = self._get_attr(content, "city")
        group.location.country = self._get_attr(content, "localized_country_name")
        group.location.state = self._get_attr(content, "state")
        group.location.latitude = self._get_attr(content, "lat")
        group.location.longitude = self._get_attr(content, "lon")
        group.location.save()

        group.save()

    def _get_attr(self, content, attr, default=None):
        """
        Returns a dictionary value by an attribute key (case insensitive).
        """
        for key in content.keys():
            if key.lower() == attr.lower():
                return content[key]
        return default
