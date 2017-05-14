from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    capital_float     = models.FloatField('capital', default=-1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    
class Index(models.Model):
    name_text = models.CharField(max_length=200)
    number_of_constituents_integer = models.IntegerField('number of constituents', default=-1)

    def __str__(self):
        return self.name_text

class Universe(models.Model):
    name_text = models.CharField(max_length=200)
    number_of_members = models.IntegerField('number of members', default=-1)
    def __str__(self):
        return self.name_text

class MomentumKPIs(models.Model):
    slope_float     = models.FloatField('slope', default=-1)
    r2_float        = models.FloatField('r2', default=-1)
    momentum_float  = models.FloatField('momentum', default=-1)
    rank_integer    = models.IntegerField('rank', default=-1)
    
    universe        = models.ManyToManyField(Universe)
    
    def __str__(self):
        return self.momentum_float    

class Instrument(models.Model):
    symbol_text = models.CharField(max_length=200, unique=True)
    name_text   = models.CharField(max_length=200, unique=True)
    
    universe    = models.ManyToManyField(Universe)
    index       = models.ManyToManyField(Index)
    kpis        = models.ManyToManyField(MomentumKPIs)
    
    def __str__(self):
        return self.name_text

    
class Price(models.Model):
    date_date   = models.DateTimeField('date', default=-1)
    open_float = models.FloatField('open price', default=-1)
    close_float = models.FloatField('close price', default=-1)
    adj_close_float = models.FloatField('adj. close price', default=-1)
    high_float = models.FloatField('high price', default=-1)
    low_float = models.FloatField('low price', default=-1)

    instrument  = models.ForeignKey(Instrument, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.close_float)
