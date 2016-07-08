from __future__ import unicode_literals
from django.contrib.auth.models import User
from public.models import Article

from django.db import models

# Create your models here.
class UserBid(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	current_bid = models.DecimalField(default=0, max_digits=9, decimal_places=2)
	maximum_bid = models.DecimalField(default=0, max_digits=9, decimal_places=2, null=True)
	created_date = models.DateTimeField(auto_now=True)
	last_bid_date = models.DateTimeField()
	is_smart_bid = models.BooleanField(default=True)