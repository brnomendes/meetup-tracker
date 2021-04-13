from django.contrib import admin
from django.contrib.auth.models import Group

from tracker.models import GroupUrlname, Location, MeetupGroup

admin.site.register(Location)
admin.site.register(GroupUrlname)
admin.site.register(MeetupGroup)
admin.site.unregister(Group)
