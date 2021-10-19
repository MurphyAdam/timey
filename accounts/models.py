from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from hashlib import md5
from .constants import USER_TYPE


class User(AbstractUser):
    """
    Custom user model with an email as unique identifier
    """
    email = models.EmailField('Email address', unique=True)
    email_verified = models.BooleanField(default=False)
    user_type = models.CharField('User account type',
                                 default=USER_TYPE[0][0],
                                 max_length=32, blank=False,
                                 null=False, choices=USER_TYPE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    @property
    def links(self):
        return {
            'avatar': self.avatar(128),
        }

    def avatar(self, size: int = 128):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=monsterid&s={}'.format(
            digest, size)

    def __str__(self):
        return self.username
