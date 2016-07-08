from django.conf.urls import url
from article import views

urlpatterns = [
	url(r'^new$', views.New.as_view(), name='new'),
	url(r'^view/(?P<article_id>[0-9]+)$', views.ViewArticle.as_view(), name='view'),
	url(r'^view$', views.ViewArticle.as_view(), name='view')
]