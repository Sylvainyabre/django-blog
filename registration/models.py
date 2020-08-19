from django.conf import settings
from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email'), unique=True)
    first_name = models.CharField(_('First name'), max_length=50, blank=True)
    last_name = models.CharField(_('Last name'), max_length=50, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='media/')
    profession = models.CharField(max_length=100, blank=True)
    interest = models.CharField(max_length=200, blank=True)
    join_date = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=
    (('Male', 'M'),
     ('Female', 'F')))
    biography = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return '{}\'s Profile '.format(self.user.email)

    # def save(self, *args, **kwargs):
    # super().save(*args, **kwargs)
    # img = Image.open(self.image.path)
    # if img.height>300 or img.width>300:
    # output_size = (300,300)
    # img.thumbnail(output_size)
    # img.save(self.image.path)
