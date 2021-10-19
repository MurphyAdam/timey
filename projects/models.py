import datetime

from django.db import models
from django.utils.text import slugify
from accounts.models import User
from .constants import status, PRIORITY_CHOICES


class Project(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(blank=True)
    description = models.TextField(null=True, blank=True)
    assigned_to = models.ManyToManyField(User)
    status = models.CharField(
        max_length=32, choices=status, default=status[0][0])
    priority = models.CharField(
        max_length=32, choices=PRIORITY_CHOICES, default=PRIORITY_CHOICES[0][0])
    dead_line = models.DateField(null=False, blank=False)

    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['name']

    @property
    def reached_deadline(self) -> bool:
        return datetime.date.today() > self.dead_line

    @property
    def days_to_deadline(self) -> int:
        if self.reached_deadline:
            return -1
        return (self.dead_line - self.created_date).days

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
