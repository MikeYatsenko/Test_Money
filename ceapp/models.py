from django.db import models
import datetime

CURRENCY_CHOICES = (
    ('EU', 'EU'),
    ('USD', 'USD'),

)

class Money(models.Model):
    name = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    course_buy = models.FloatField(max_length=4)
    course_sell = models.FloatField(max_length=4)
    date_from = models.DateField(default=datetime.date.today)
    date_to = models.DateField(default=datetime.date.today)



