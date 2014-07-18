from django.db import models

# Create your models here.

class Symbol(models.Model):
	symbol = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	is_const = models.BooleanField(default=False)
	def __unicode__(self):
		return self.symbol

class Equation(models.Model):
	equation = models.CharField(max_length=500)
	name = models.CharField(max_length=150)
	def __unicode__(self):
		return self.equation

class SymEq(models.Model):
	sym = models.ForeignKey(Symbol)
	eq = models.ForeignKey(Equation)
	def __unicode__(self):
		return '%s contains: %s' % (self.eq.equation, self.sym.symbol)
