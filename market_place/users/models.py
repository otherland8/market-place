from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class UserProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=128, null=True, blank=True)
	date_of_birth = models.DateTimeField(null=True, blank=True, default=None)
	picture_path = models.CharField(max_length=128, null=True, blank=True)
	followers = models.ManyToManyField(User, related_name='user_followers')
