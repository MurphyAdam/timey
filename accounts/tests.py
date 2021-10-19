from rest_framework.test import APITestCase, APIClient
from .models import User


class AccountTests(APITestCase):

    client = APIClient()

    username = 'test_user1'
    email = 'test.user1@gmail.com'
    password = '@1234xyz@'
    user_type = 'regular'
    data = data = {'username': username,
                   'email': email,
                   'password': password,
                   'user_type': user_type,
                   }

    def create_user(self):
        return User.objects.create_user(**self.data)

    def test_users_exist(self):
        self.assertEqual(User.objects.count(), 0)
        self.create_user()

    def test_create_user_without_api(self):
        """
        Ensure we can create a new account object and login.
        """
        self.user = self.create_user()
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.email, self.email)

    def test_login(self):
        """
        User can login in with correct credintials
        """
        self.user = self.create_user()
        self.assertTrue(self.client.login(
            email=self.email, password=self.password))

    def test_delete_user(self):
        """
        We can delete a user
        """
        self.user = self.create_user()
        self.user.delete()
        self.assertEqual(User.objects.count(), 0)
