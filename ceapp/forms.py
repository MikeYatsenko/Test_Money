from django.forms import ModelForm
from .models import Money

class MoneyForm(ModelForm):
    class Meta:
        model = Money
        fields = ['name', 'course_buy', 'course_sell', 'date_from', 'date_to']
