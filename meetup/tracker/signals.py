from django.db.models.signals import post_save
from django.dispatch import receiver

from tracker.integration.client_api import UpdateMeetupGroup
from tracker.models import GroupUrlname


@receiver(post_save, sender=GroupUrlname)
def save_group_urlname(sender, instance, **kwargs):
    """
    When a new urlname is added, in a thread, we synchronize the
    group data and events with meetup.com.
    """
    UpdateMeetupGroup(instance).start()
