from django.db import models


class Location(models.Model):
    """
    Model that represents a Location.
    """

    city = models.CharField(max_length=256, blank=False)
    name = models.CharField(max_length=256, blank=True)
    address_1 = models.CharField(max_length=256, blank=True)
    address_2 = models.CharField(max_length=256, blank=True)
    state = models.CharField(max_length=256, blank=True)
    country = models.CharField(max_length=256, blank=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True)

    def __str__(self):
        return f"{self.city} {self.name}"


class GroupUrlname(models.Model):
    """
    Model that represents a Group urlname in the Meetup.
    The urlnames must be added by administrators to track groups.
    """

    urlname = models.CharField(max_length=256, blank=False)

    def __str__(self) -> str:
        return self.urlname


class MeetupGroup(models.Model):
    """
    Model that represents a Meetup Group.
    """

    name = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=256, blank=True)
    link = models.CharField(max_length=1024, blank=True)
    photo_link = models.CharField(max_length=1024, blank=True)
    member_count = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False)
    urlname = models.OneToOneField(GroupUrlname, on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return self.name


class MeetupEvent(models.Model):
    """
    Model that represents a Meetup Event.
    """

    name = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=256, blank=True)
    link = models.CharField(max_length=1024, blank=True)
    time = models.IntegerField(blank=True, null=True)
    is_online_event = models.BooleanField(default=False)
    duration = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    group = models.ForeignKey(
        MeetupGroup, related_name="events", on_delete=models.CASCADE, null=False
    )

    def __str__(self) -> str:
        return self.name
