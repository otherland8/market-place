from public.models import Category

def get_layout_context(request, active_view):
	top_categories = Category.objects.filter(parent_category__parent_category=None);
	context = {
		'top_categories': top_categories,
		'is_authenticated': request.user.is_authenticated(),
		'username': request.user.username,
		'active_view': active_view
	}
	return context