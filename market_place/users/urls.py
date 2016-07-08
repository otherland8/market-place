from django.conf.urls import url
from users import views

urlpatterns = [
	url(r'^profile$', views.Index.as_view(), name='profile'),
	url(r'^profile/(?P<username>[a-zA-Z0-9]+)$', views.ViewProfile.as_view(), name='view'),
	url(r'^change_password$', views.ChangePassword.as_view(), name="change_password")
]