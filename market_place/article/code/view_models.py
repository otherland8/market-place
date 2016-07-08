from django import forms

class ArticleViewModel(forms.Form):
	title = forms.CharField()
	category = forms.IntegerField()
	description = forms.CharField(required=False)
	starting_price = forms.DecimalField(max_digits=9, decimal_places=2)
	buyout_price = forms.DecimalField(max_digits=9, decimal_places=2)
	condition = forms.IntegerField()
	expiry_date = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'])


class PlaceBidViewModel(forms.Form):
	article_id = forms.IntegerField()
	bid = forms.DecimalField(max_digits=9, decimal_places=2)
	is_smart_bid = forms.BooleanField(required=False)