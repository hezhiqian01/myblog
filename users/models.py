from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        pass

    def __unicode__(self):
        return self.username
