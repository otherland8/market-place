from django.contrib.auth.models import User
from view_models import ArticleViewModel, PlaceBidViewModel
from public.models import Article, Category
from article.models import UserBid
import datetime


def save_article(request):
	view_model = ArticleViewModel(data=request.POST)
	if view_model.is_valid():
		category = Category.objects.get(pk=view_model.cleaned_data['category'])
		created_by = User.objects.get(username=request.user.username)
		article = Article(
			title=view_model.cleaned_data['title'],
			category=category,
			description=view_model.cleaned_data['description'],
			starting_price=view_model.cleaned_data['starting_price'],
			buyout_price=view_model.cleaned_data['buyout_price'],
			currency='USD',
			condition=view_model.cleaned_data['condition'],
			expiry_date=view_model.cleaned_data['expiry_date'],
			last_modified_date=datetime.datetime.now(),
			created_by=created_by
			)
		article.save()
		return article.id
	return None

def save_user_bid(request):
	view_model = PlaceBidViewModel(data=request.POST)
	if view_model.is_valid():
		try:
			bid = UserBid.objects.get(user__username=request.user.username, article__id=view_model.cleaned_data['article_id'])
			bid.current_bid = view_model.cleaned_data['bid']
			bid.last_bid_date = datetime.datetime.now()
			bid.save()
		except Exception, e:
			user = User.objects.get(username=request.user.username)
			article = Article.objects.get(pk=view_model.cleaned_data['article_id'])
			bid = UserBid(
				user=user, 
				article=article, 
				current_bid=view_model.cleaned_data['bid'],
				maximum_bid=view_model.cleaned_data['bid'],
				last_bid_date=datetime.datetime.now(),
				is_smart_bid=view_model.cleaned_data['is_smart_bid'])
			bid.save()
		
		
		