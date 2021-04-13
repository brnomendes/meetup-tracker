from django.contrib import admin
from django.contrib.auth.models import Group

from tracker.models import GroupUrlname, Location, MeetupEvent, MeetupGroup

admin.site.register(Location)
admin.site.register(GroupUrlname)
admin.site.register(MeetupGroup)
admin.site.register(MeetupEvent)
admin.site.unregister(Group)
