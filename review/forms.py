from django.forms import ModelForm
from review.models import Item

class ReviewForm(ModelForm):
    class Meta:
        model = Item
        fields = ["review", "rating"]