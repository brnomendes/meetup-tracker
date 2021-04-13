from django.contrib import admin
from django.urls import path
from tracker.views import LocationList, MeetupGroupList

urlpatterns = [
    path("admin/", admin.site.urls),
    path("locations/", LocationList.as_view()),
    path("groups/", MeetupGroupList.as_view()),
]
