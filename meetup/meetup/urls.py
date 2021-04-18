from django.contrib import admin
from django.urls import path
from tracker.views import LocationList, MeetupEventList, MeetupGroupList, MeetupUpdate

urlpatterns = [
    path("admin/", admin.site.urls),
    path("locations/", LocationList.as_view()),
    path("groups/", MeetupGroupList.as_view()),
    path("groups/<int:pk>/events/", MeetupEventList.as_view()),
    path("groups/<int:pk>/update/", MeetupUpdate.as_view()),
]
