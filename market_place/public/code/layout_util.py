from public.models import Category

def get_layout_context(request, active_view):
	root_category = Category.objects.get(parent_category=None)
	top_categories = Category.objects.filter(parent_category=root_category)
	context = {
		'top_categories': top_categories,
		'is_authenticated': request.user.is_authenticated(),
		'username': request.user.username,
		'active_view': active_view,
		'can_create_articles': request.user.has_perm('public.add_article')
	}
	return context