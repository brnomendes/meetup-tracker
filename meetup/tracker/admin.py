from django.contrib import admin
from django.contrib.auth.models import Group

from tracker.models import GroupUrlname, Location

admin.site.register(Location)
admin.site.register(GroupUrlname)
admin.site.unregister(Group)
