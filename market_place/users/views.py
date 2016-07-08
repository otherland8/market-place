from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from public.models import Category
from .models import UserProfile
from .view_models import ProfileEditViewModel, ChangePasswordViewModel
from public.code.layout_util import get_layout_context
from users.code.user_profile_util import save_user_profile

class Index(View):

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect('/public/signin')

		context = get_layout_context(request, 'users/profile');

		try:
			user_profile = UserProfile.objects.get(user__username=request.user.username);
		except (KeyError, UserProfile.DoesNotExist):
			user = User.objects.get(username=request.user.username)
			user_profile = UserProfile(user=user)
			user_profile.save()

		if user_profile.picture_path:
			user_profile.picture_url = 'public/upload/users/{0}/{1}'.format(request.user.username, user_profile.picture_path)
		else:
			user_profile.picture_url = 'public/upload/no_profile.png'
		context['user_profile'] = user_profile
		return render(request, 'users/index.html', context)

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect('/public/signin')
		context = get_layout_context(request, 'users/profile')
		user_profile = save_user_profile(request)
		if user_profile:
			context['user_profile'] = user_profile
		return render(request, 'users/index.html', context)


class ViewProfile(View):

	def get(self, request, username, *args, **kwargs):
		print('username: {0}'.format(username))
		context = get_layout_context(request, None)
		try:
			user_profile = UserProfile.objects.get(user__username=username)
			if user_profile.picture_path:
				user_profile.picture_url = 'public/upload/users/{0}/{1}'.format(request.user.username, user_profile.picture_path)
			else:
				user_profile.picture_url = 'public/upload/no_profile.png'
			context['user_profile'] = user_profile
		except Exception, e:
			pass
			
		return render(request, 'users/view.html', context)


class ChangePassword(View):

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect('/public/signin')
		view_model = ChangePasswordViewModel(data=request.POST)
		context = get_layout_context(request, 'users/profile')
		if view_model.is_valid():
			user = User.objects.get(username=request.user.username)
			if authenticate(username=request.user.username, password=view_model.cleaned_data['old_password']) is None:
				context['change_password_error'] = 'Old password is wrong!'
			elif view_model.cleaned_data['new_password'] != view_model.cleaned_data['repeat_new_password']:
				context['change_password_error'] = 'New password and repeat new password must match!'
			else:
				user.set_password(view_model.cleaned_data['new_password'])
				user.save()
		user_profile = UserProfile.objects.get(user__username=request.user.username)
		if user_profile.picture_path:
			user_profile.picture_url = 'public/upload/users/{0}/{1}'.format(request.user.username, user_profile.picture_path)
		else:
			user_profile.picture_url = 'public/upload/no_profile.png'
		context['user_profile'] = user_profile
		return render(request, 'users/index.html', context)
