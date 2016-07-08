from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email
from django import forms

from code.layout_util import get_layout_context

from .models import Category


class Index(View):
	def get(self, request, *args, **kwargs):
		context = get_layout_context(request, 'public/index')
		return render(request, 'public/index.html', context)


class Signup(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'public/signup.html')

	def post(self, request, *args, **kwargs):
		context = {
			'error_message': ''
		}
		if request.POST['password'] != request.POST['repeat_password']:
			context['error_message'] = 'Passwords did not match!'
			return render(request, 'public/signup.html', context)

		try:
			validate_email(request.POST['email'])
		except forms.ValidationError:
			context['error_message'] = 'Invalid email entered!'
			return render(request, 'public/signup.html', context)
		requested_username = request.POST['username']
		try:
			user = User.objects.get(username=requested_username)
			context['error_message'] = 'User with username "{0}" already exists!'.format(requested_username)
			return render(request, 'public/signup.html', context)
		except(KeyError, User.DoesNotExist):
			user = User.objects.create_user(requested_username, request.POST['email'], request.POST['password'])
			return redirect('/users/profile')


class Signin(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'public/signin.html')

	def post(self, request, *args, **kwargs):
		context = {
			'error_message': ''
		}
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				login(request, user)
				redirect_url = request.GET.get('next')
				if not redirect_url:
					redirect_url = '/users/profile'
				return redirect(redirect_url)
			else:
				context['error_message'] = 'Your account is inactive!'
				return render(request, 'public/signin.html', context)
		else:
			context['error_message'] = 'Invalid username and/or password!'
			return render(request, 'public/signin.html', context)

class Signout(View):
	def get(self, request, *args, **kwargs):
		logout(request)
		return redirect('/public')
