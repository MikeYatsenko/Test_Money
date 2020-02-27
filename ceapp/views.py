from .forms import MoneyForm
from .models import Money
from django.views import generic
from django.urls import reverse_lazy
import datetime

class CreateMoneyView(generic.CreateView):
    form_class = MoneyForm
    model = Money
    def get_success_url(self):
           return ('front_page')


class MoneyFirstPageView(generic.ListView):
    model = Money
    template_name = 'ceapp/front_page.html'
    context_object_name = 'money_list'
    queryset = Money.objects.filter(date_from=datetime.date.today())

class MoneyListViewEU(generic.ListView):
    model = Money
    context_object_name = 'money_list'
    queryset = Money.objects.filter(name='EU').order_by('-date_from')
    template_name = 'ceapp/list_eu.html'
    paginate_by = 4

class MoneyListViewUSD(generic.ListView):
    model = Money
    context_object_name = 'money_list'
    queryset = Money.objects.filter(name='USD').order_by('-date_from')
    template_name = 'ceapp/list_usd.html'
    paginate_by = 4

class MoneyListDelete(generic.DeleteView):
    model = Money
    success_url = reverse_lazy('front_page')
class MoneyUpdateList(generic.UpdateView):
    form_class = MoneyForm
    model = Money
    success_url = reverse_lazy('front_page')