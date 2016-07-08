from django.conf.urls import url
from public import views

urlpatterns = [
	url(r'^$', views.Index.as_view(), name='index'),
	url(r'^signup$', views.Signup.as_view(), name='signup'),
	url(r'^signin$', views.Signin.as_view(), name='signin'),
	url(r'^signout$', views.Signout.as_view(), name='signout')
]