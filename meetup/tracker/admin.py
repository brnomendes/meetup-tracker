from django.contrib import admin
from django.contrib.auth.models import Group

from tracker.models import City, Country, GroupUrlname, Location, MeetupEvent, MeetupGroup

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Location)
admin.site.register(GroupUrlname)
admin.site.register(MeetupGroup)
admin.site.register(MeetupEvent)
admin.site.unregister(Group)
