from django.db import models

# Create your models here.
class Symbol(models.Model):
    symbol = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    constant = models.BooleanField(default=False)
    def __unicode__(self):
    	return self.name

class Equation(models.Model):
    latex = models.CharField(max_length=500)
    name = models.CharField(max_length=150)
    def __unicode__(self):
    	return self.name

class SymbolEquation(models.Model):
	symbol = models.ForeignKey(Symbol)
	equation = models.ForeignKey(Equation)
	def __unicode__(self):
		return self.symbol.symbol + " : " +  self.equation.latex