import datetime
from datetime import datetime as dt

from rest_framework.test import APITestCase, APIClient
from freezegun import freeze_time

from accounts.models import User
from .models import Project


@freeze_time("2021-11-14")
class ProjectTests(APITestCase):

    client = APIClient()

    def setUp(self) -> None:
        self.user = self.create_user()
        self.client.force_authenticate(user=self.user)
        self.project = None
        return super().setUp()

    name = 'IOT on Blockchain'
    dead_line = datetime.date(2021, 11, 21)
    data = {
        'name': name,
        'dead_line': dead_line,
    }

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

    def create_project(self):
        project = Project.objects.create(**self.data)
        project.assigned_to.add(self.user)
        return project

    def test_create_project_without_api(self):
        """
        Ensure we can create a new project object.
        """
        self.project = self.create_project()
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(self.project.name, 'IOT on Blockchain')
        self.assertEqual(self.project.dead_line,
                         datetime.date(2021, 11, 21))
        self.assertFalse(self.project.reached_deadline)
        self.assertEqual(self.project.days_to_deadline, 7)

    def test_create_project_with_api(self):
        """
        Ensure we can create a new project object with an
        API call, and we test data fields.
        """
        url = 'http://127.0.0.1:8000/api/projects'
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, 201)
        self.project = response.data
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(self.project['name'], 'IOT on Blockchain')
        self.assertEqual(self.project['slug'], 'iot-on-blockchain')
        dead_line = dt.strptime(self.project['dead_line'], '%Y-%m-%d').date()
        self.assertEqual(dead_line,
                         datetime.date(2021, 11, 21))
        self.assertFalse(self.project['reached_deadline'])
        self.assertEqual(self.project['days_to_deadline'], 7)

    def test_delete_project(self):
        """
        We can delete a user
        """
        self.project = self.create_project()
        self.assertEqual(Project.objects.count(), 1)
        self.project.delete()
        self.assertEqual(Project.objects.count(), 0)
