from __future__ import unicode_literals

from django.db import models


class User(models.Model):
	username = models.CharField(max_length=64)
	password = models.CharField(max_length=256)
	first_name = models.CharField(max_length=24)
	last_name = models.CharField(max_length=24)
	email = models.EmailField()
	created_date = models.DateTimeField(auto_now=True)
	active = models.BooleanField()
	followers = models.ManyToManyField('self', related_name='user_=followers')


class Category(models.Model):
	parent_category = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=128)


class Article(models.Model):
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=256)
	description = models.TextField()
	quantity = models.IntegerField(default=0)
	sold = models.IntegerField(default=0)
	price = models.DecimalField(default=0, max_digits=9, decimal_places=2)
	currency = models.CharField(max_length=4)
	condition = models.IntegerField()
	created_date = models.DateTimeField(auto_now=True)
	last_modified_date = models.DateTimeField()
	rating = models.FloatField(default=0)
	active = models.BooleanField()
	followers = models.ManyToManyField(User, related_name='article_followers')


class Comment(models.Model):
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	text = models.TextField()
	created_date = models.DateTimeField(auto_now=True)
	last_modified_date = models.DateTimeField()
