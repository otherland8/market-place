from django import forms

class ProfileEditViewModel(forms.Form):
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)
	email = forms.CharField(required=False)
	address = forms.CharField(required=False)
	date_of_birth = forms.DateField(required=False)
	picture = forms.FileField(required=False)


class ChangePasswordViewModel(forms.Form):
	old_password = forms.CharField(required=True)
	new_password = forms.CharField(required=True)
	repeat_new_password = forms.CharField(required=True)