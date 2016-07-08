from django.shortcuts import render, redirect
from django.db.models import Max
from django.views.generic import View
from public.models import Article
from models import UserBid
import datetime

from public.code.layout_util import get_layout_context
from code.article_util import save_article, save_user_bid
# Create your views here.

ARTICLE_CONDITIONS = {
	1: "New",
	2: "Used"
}

class New(View):
	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect('/public/signin')
		context = get_layout_context(request, None)
		context['conditions'] = ARTICLE_CONDITIONS.items()
		return render(request, 'article/new.html', context)

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect('/public/signin')
		article_id = save_article(request)
		if article_id == None:
			article_id = 0
		return redirect('view/{0}'.format(article_id))


class ViewArticle(View):
	def get(self, request, article_id, *args, **kwargs):
		context = get_layout_context(request, None)
		try:
			article = Article.objects.get(pk=article_id)
			context['article'] = article
			highest_bids = UserBid.objects.filter(article=article).order_by('-current_bid')
			if len(highest_bids) > 0:
				highest_bid = highest_bids[0]
				context['highest_bid'] = highest_bid
			
			article.condition_name = ARTICLE_CONDITIONS[article.condition]
			article.can_place_bid = request.user.is_authenticated() and request.user.username != article.created_by.username
			article.picture_url = 'public/upload/no-image.png'
		except Exception, e:
			raise e
		return render(request, 'article/view.html', context)

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect('/public/signin')
		save_user_bid(request)
		return redirect('view/{0}'.format(request.POST.get('article_id')))
