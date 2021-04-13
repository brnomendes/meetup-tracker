from django.contrib import admin
from django.urls import path
from tracker.views import LocationList

urlpatterns = [
    path("admin/", admin.site.urls),
    path("locations/", LocationList.as_view()),
]
