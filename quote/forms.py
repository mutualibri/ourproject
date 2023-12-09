from django.forms import ModelForm
from quote.models import Quotes

class QuoteForm(ModelForm):
    class Meta:
        model = Quotes
        fields = ["book_name", "quotes"]