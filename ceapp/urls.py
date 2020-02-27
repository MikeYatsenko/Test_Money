from . import views
from django.urls import path
urlpatterns = [
      path("create/", views.CreateMoneyView.as_view(), name="money_form"),
      path("create/front_page", views.MoneyFirstPageView.as_view(), name="front_page"),
      path("", views.MoneyFirstPageView.as_view(), name="front_page"),
      path("list_eu/", views.MoneyListViewEU.as_view(), name="list_eu"),
      path("list_usd/", views.MoneyListViewUSD.as_view(), name="list_usd"),
      path("list_eu/<int:pk>/delete", views.MoneyListDelete.as_view(), name="money_delete_confirm"),
      path("list_usd/<int:pk>/delete", views.MoneyListDelete.as_view(), name='money_delete_confirm'),
      path("list_eu/<int:pk>/update", views.MoneyUpdateList.as_view(), name='money_update'),
      path("list_usd/<int:pk>/update", views.MoneyUpdateList.as_view(), name='money_update'),
]
