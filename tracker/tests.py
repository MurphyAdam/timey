import datetime
from datetime import datetime as dt

from django.utils import timezone
from rest_framework.test import APITestCase, APIClient
from freezegun import freeze_time

from accounts.models import User
from projects.models import Project
from .models import Tracker


@freeze_time("2021-11-14 03:04:05")
class TrackerTests(APITestCase):

    client = APIClient()
    tracker_entry = None

    def setUp(self) -> None:
        self.user = self.create_user()
        self.project = self.create_project()
        self.project.assigned_to.add(self.user)
        self.client.force_authenticate(user=self.user)
        return super().setUp()

    def create_project(self):
        name = 'IOT on Blockchain'
        dead_line = datetime.date(2021, 11, 21)
        data = {
            'name': name,
            'dead_line': dead_line,
        }
        return Project.objects.create(**data)

    def create_user(self):
        username = 'test_user1'
        email = 'test.user1@gmail.com'
        password = '@1234xyz@'
        user_type = 'regular'
        data = {'username': username,
                'email': email,
                'password': password,
                'user_type': user_type,
                }
        return User.objects.create_user(**data)

    def create_tracker_entry(self):
        start_time = timezone.now()
        tracker = Tracker.objects.create(user=self.user,
                                         project=self.project,
                                         start_time=start_time)
        return tracker

    def test_create_tracker_entry_without_api(self):
        """
        Ensure we can create a new tracker object.
        """
        self.tracker_entry = self.create_tracker_entry()
        self.assertEqual(Tracker.objects.count(), 1)
        self.assertEqual(self.tracker_entry.user.username, 'test_user1')
        self.assertEqual(self.tracker_entry.start_time,
                         timezone.now())
        self.assertTrue(self.tracker_entry.is_paused)

    def test_create_tracker_entry_with_api(self):
        """
        Ensure we can create a new tracker object with an
        API call, and we test data fields.
        """
        url = 'http://127.0.0.1:8000/api/tracker'
        start_time = timezone.now()

        data = {
            'user': self.user.id,
            'project': self.project.id,
            'start_time': start_time
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.tracker_entry = response.json()
        self.assertEqual(Tracker.objects.count(), 1)
        self.assertEqual(
            self.tracker_entry['project']['name'], 'IOT on Blockchain')
        dead_line = dt.strptime(
            self.tracker_entry['project']['dead_line'], '%Y-%m-%d').date()
        self.assertEqual(dead_line,
                         datetime.date(2021, 11, 21))
        self.assertEqual(Tracker.objects.count(), 1)
        self.assertEqual(self.tracker_entry['user']['username'], 'test_user1')
        self.assertEqual(
            self.tracker_entry['start_time'], '2021-11-14T03:04:05Z')
        self.assertTrue(self.tracker_entry['is_paused'])

    def test_delete_tracker_entry(self):
        """
        We can a tracker entry
        """
        self.tracker_entry = self.create_tracker_entry()
        self.assertEqual(Tracker.objects.count(), 1)
        self.tracker_entry.delete()
        self.assertEqual(Tracker.objects.count(), 0)
