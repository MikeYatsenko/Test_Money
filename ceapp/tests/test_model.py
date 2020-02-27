from django.test import TestCase
from ceapp.models import Money
import datetime

class MoneyModelTest(TestCase):


     @classmethod
     def setUpTestData(cls):
        Money.objects.create(name='EU', course_buy='25.04', course_sell='25.25',
                              date_from=datetime.date.today(), date_to=datetime.date.today())

     def test_add_today_date(self):
         Money.objects.create(name='EU', course_buy='27.04', course_sell='25.25',
                              date_from=datetime.date.today(), date_to=datetime.date.today())
         money =Money.objects.get(id=2)
         self.assertEquals(money.course_buy, 27.04)

     def test_create_some_date(self):
         Money.objects.create(name='EU', course_buy='27.04', course_sell='25.25',
                              date_from='2020-02-02', date_to='2020-02-04')
         money =Money.objects.get(id=3)
         self.assertEquals(money.course_buy, 27.04)





