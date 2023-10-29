from django.forms import ModelForm
<<<<<<< HEAD:lend/forms.py
from lend.models import Lend
from django import forms
from django.utils import timezone

class ProductForm(ModelForm):
    class Meta:
        model = Lend
        fields = ['user', 'book', 'start_date', 'end_date', 'number']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget = forms.HiddenInput()  # Hide start_date field
        self.fields['end_date'].widget = forms.HiddenInput()    # Hide end_date field
        self.fields['number'].widget = forms.HiddenInput()      # Hide number field
        self.fields['start_date'].initial = timezone.now()  # Set start_date to the current date
        self.fields['end_date'].initial = timezone.now() + timezone.timedelta(days=7)  # Set end_date to 7 days later
        self.fields['number'].initial = self.instance.book.pk  # Set number to book.pk
=======
from review.models import Item

class ReviewForm(ModelForm):
    class Meta:
        model = Item
        fields = ["review", "rating"]
>>>>>>> 57b6f08b8a83048d65c3e314cbe7621ccaf1a637:review/forms.py
