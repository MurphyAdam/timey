from projects.models import Project
from django.db import models
from django.utils import timezone
from accounts.models import User
from .constants import STATUSES


class Tracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=32, choices=STATUSES, default=STATUSES[0][0])
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True, db_index=True)
    seconds_paused = models.PositiveIntegerField(default=0)
    pause_time = models.DateTimeField(blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)
    hours = models.DecimalField(max_digits=11, decimal_places=5, default=0)

    class Meta:
        unique_together = ('user', 'project',)

    def get_total_seconds(self):
        """
        Determines the total number of seconds between the starting and
        ending times of this entry. If the entry is paused, the end_time is
        assumed to be the pause time. If the entry is active but not paused,
        the end_time is assumed to be now.
        """
        start = self.start_time
        end = self.end_time
        if not end:
            if self.is_paused:
                end = self.pause_time
            else:
                end = timezone.now()
        delta = end - start
        if self.is_paused:
            # get_paused_seconds() takes elapsed time into account, which we do not want
            # in this case, so subtract seconds_paused instead to account for previous pauses
            seconds = delta.seconds - self.seconds_paused
        else:
            seconds = delta.seconds - self.get_paused_seconds()
        return seconds + (delta.days * 86400)

    def get_paused_seconds(self):
        """
        Returns the total seconds that this entry has been paused. If the
        entry is currently paused, then the additional seconds between
        pause_time and now are added to seconds_paused. If pause_time is in
        the future, no extra pause time is added.
        """
        if self.is_paused:
            date = timezone.now()
            delta = date - self.pause_time
            extra_pause = max(0, delta.seconds + (delta.days * 24 * 60 * 60))
            return self.seconds_paused + extra_pause
        return self.seconds_paused

    @property
    def total_hours(self):
        """
        Determined the total number of hours worked in this entry
        """
        total = self.get_total_seconds() / 3600.0
        # in case seconds paused are greater than the elapsed time
        if total < 0:
            total = 0
        return total

    @property
    def is_paused(self):
        """
        Determine whether or not this entry is paused
        """
        return bool(self.pause_time)

    def pause(self):
        """
        If this entry is not paused, pause it.
        """
        if not self.is_paused:
            self.pause_time = timezone.now()

    def pause_all(self):
        """
        Pause all open entries
        """
        entries = self.user.timepiece_entries.filter(end_time__isnull=True)
        for entry in entries:
            entry.pause()
            entry.save()

    def unpause(self, date=None):
        if self.is_paused:
            if not date:
                date = timezone.now()
            delta = date - self.pause_time
            self.seconds_paused += delta.seconds
            self.pause_time = None

    def toggle_paused(self):
        """
        Toggle the paused state of this entry.  If the entry is already paused,
        it will be unpaused; if it is not paused, it will be paused.
        """
        if self.is_paused:
            self.unpause()
        else:
            self.pause()

    @property
    def is_closed(self):
        """
        Determine whether this entry has been closed or not
        """
        return bool(self.end_time)

    def __str__(self):
        return f'Tracker for {self.user.username} on project {self.project.name}'
