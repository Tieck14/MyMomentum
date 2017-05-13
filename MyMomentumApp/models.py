from django.db import models



class Instrument(models.Model):
    symbol_text = models.CharField(max_length=200)
    name_text   = models.CharField(max_length=200)
    def __str__(self):
        return self.name_text

class Price(models.Model):
    date_date   = models.DateTimeField('date')
    close_float = models.FloatField('close price')

    instrument  = models.ForeignKey(Instrument, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.close_float)
