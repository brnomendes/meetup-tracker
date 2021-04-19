from threading import Thread

import requests
from django.core.exceptions import ObjectDoesNotExist

from tracker.models import City, Country, Location, MeetupEvent, MeetupGroup


class UpdateMeetupGroup(Thread):
    API_URL = "https://api.meetup.com"
    EVENT_STATUS = ["past", "upcoming"]

    def __init__(self, group_urlname):
        Thread.__init__(self)
        self._group_urlname = group_urlname
        self._group_url = f"{self.API_URL}/{self._group_urlname.urlname}"

    def run(self):
        self.update_group()

    def update_group(self):
        """
        Updates the group and events model with the data from the Meetup API.
        """
        response = requests.get(self._group_url)
        if response.status_code != 200:
            return
        content = response.json()
        group = self._update_group_data(content)
        self._update_events(group)

    def _update_events(self, group):
        """
        Updates the events model with the data from the Meetup API.
        """
        response = requests.get(
            f"{self._group_url}/events", params={"status": ",".join(self.EVENT_STATUS)}
        )
        if response.status_code != 200:
            return
        content = response.json()
        self._update_events_data(group, content)

    def _update_group_data(self, content):
        """
        Receive JSON from the Meetup API and create or update the group model.
        """
        try:
            group = MeetupGroup.objects.get(urlname=self._group_urlname)
        except ObjectDoesNotExist:
            group = MeetupGroup()
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

        group.location.latitude = self._get_attr(content, "lat")
        group.location.longitude = self._get_attr(content, "lon")
        self._update_location_city(
            group.location,
            self._get_attr(content, "city"),
            self._get_attr(content, "localized_country_name"),
        )
        group.location.save()

        group.save()
        return group

    def _update_events_data(self, group, content):
        """
        Receive JSON from the Meetup API and create or update the event models of a group.
        """
        events = []
        for entry in content:
            try:
                event_id = int(self._get_attr(entry, "id"))
            except ValueError:
                continue

            try:
                event = MeetupEvent.objects.get(id=event_id)
            except ObjectDoesNotExist:
                event = MeetupEvent(id=event_id)

            event.name = self._get_attr(entry, "name")
            event.link = self._get_attr(entry, "link", "")
            event.description = self._get_attr(entry, "description", "")
            event.status = self._get_attr(entry, "status")
            event.time = self._get_attr(entry, "time")
            event.duration = self._get_attr(entry, "duration")
            event.is_online_event = self._get_attr(entry, "is_online_event")

            venue = self._get_attr(entry, "venue", {})
            city_name = self._get_attr(venue, "city")
            country_name = self._get_attr(venue, "localized_country_name")
            if city_name and country_name:
                if not event.location:
                    event.location = Location()
                event.location.latitude = self._get_attr(venue, "lat")
                event.location.longitude = self._get_attr(venue, "lon")
                event.location.address_1 = self._get_attr(venue, "address_1", "")
                event.location.address_2 = self._get_attr(venue, "address_2", "")
                self._update_location_city(event.location, city_name, country_name)
                event.location.save()

            events.append(event)
        group.events.set(events, bulk=False)
        group.save()

    def _update_location_city(self, location, city_name, country_name):
        """
        Update or create city of location.
        """
        try:
            country = Country.objects.get(name=country_name)
        except ObjectDoesNotExist:
            country = Country(name=country_name)
            country.save()
        try:
            city = City.objects.get(name=city_name)
        except ObjectDoesNotExist:
            city = City(name=city_name, country=country)
            city.save()
        location.city = city

    def _get_attr(self, content, attr, default=None):
        """
        Returns a dictionary value by an attribute key (case insensitive).
        """
        for key in content.keys():
            if key.lower() == attr.lower():
                return content[key]
        return default
