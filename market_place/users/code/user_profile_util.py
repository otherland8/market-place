import os

PROFILE_PICTURE_UPLOAD_PATH_TEMPLATE = os.path.abspath('public/static/public/upload/users/{0}/{1}')

from users.models import UserProfile
from users.view_models import ProfileEditViewModel

def save_user_profile(request):
	view_model = ProfileEditViewModel(data=request.POST, files=request.FILES);
	if (view_model.is_valid()):
		user_profile = UserProfile.objects.get(user__username=request.user.username)
		user_profile.user.email = view_model.cleaned_data['email']
		user_profile.user.first_name = view_model.cleaned_data['first_name']
		user_profile.user.last_name = view_model.cleaned_data['last_name']
		user_profile.address = view_model.cleaned_data['address']
		user_profile.date_of_birth = view_model.cleaned_data['date_of_birth']
		user_profile.picture_path = save_profile_picture(view_model.cleaned_data['picture'], request.user.username)
		user_profile.user.save()
		user_profile.save()
		return user_profile
	return None

def save_profile_picture(f, username):
	try:
		directory = PROFILE_PICTURE_UPLOAD_PATH_TEMPLATE.format(username, "")
		file_path = PROFILE_PICTURE_UPLOAD_PATH_TEMPLATE.format(username, f.name)
		if not os.path.exists(directory):
			os.makedirs(directory)
		if f:
			with open(file_path, 'wb+') as destination:
				destination.write(f.read())
			return f.name
		return ""
	except Exception, e:
		raise
	else:
		pass
	finally:
		pass