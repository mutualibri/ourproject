from django import forms
from lend.models import Lend
from django.utils import timezone

class LendForm(forms.ModelForm):
    class Meta:
        model = Lend
        fields = []

    def __init__(self, user, book_id, *args, **kwargs):
        super(LendForm, self).__init__(*args, **kwargs)
        current_date = timezone.now()
        future_date = current_date + timezone.timedelta(days=7)
        self.initial['start_date'] = current_date
        self.initial['end_date'] = future_date
        self.user = user
        self.book_id = book_id
        # Set number to the book_id
        self.initial['number'] = book_id

    def save(self, commit=True):
        lend = super(LendForm, self).save(commit=False)
        lend.user = self.user
        lend.book_id = self.book_id
        lend.start_date = self.initial['start_date']
        lend.end_date = self.initial['end_date']
        lend.number = self.initial['number']  # Isi number dari initial
        if commit:
            lend.save()
        return lend


class BookFilterForm(forms.Form):
    title = forms.CharField(required=False)
    author = forms.CharField(required=False)