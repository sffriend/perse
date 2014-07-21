from django.db import models

# models
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
    	
class Section(models.Model):
	name = models.CharField(max_length=100)
	ch_num = models.IntegerField()
	def __unicode__(self):
		return self.name

class Exercise(models.Model):
	sec = models.ForeignKey(Section)
	text = models.TextField()
	img = models.CharField(max_length = 100)
	title = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.title

class Tag(models.Model):
	name = models.CharField(max_length=100)
	def __unicode__(self):
		return self.name
		
#Linking Tabels

#Link symbols and equations
class SymbolEquation(models.Model):
	symbol = models.ForeignKey(Symbol)
	equation = models.ForeignKey(Equation)
	def __unicode__(self):
		return self.symbol.symbol + " : " +  self.equation.latex
		
#Link Sections and Equations
class SectionEqn(models.Model):
	section = models.ForeignKey(Section)
	equation = models.ForeignKey(Equation)
	def __unicode__(self):
		return self.section.name + " : " +  self.equation.latex

#Link sections and symbols
class SectionSym(models.Model):
	section = models.ForeignKey(Section)
	symbol = models.ForeignKey(Symbol)
	def __unicode__(self):
		return self.section.name + " : " +  self.symbol.symbol

#Link tags and exercises
class TagLink(models.Model):
	tag = models.ForeignKey(Tag)
	exc = models.ForeignKey(Exercise)
	def __unicode__(self):
		return self.exc.title + " : " +  self.tag.name

#Link equations and exercises
class ExcEqn(models.Model):
	exc = models.ForeignKey(Exercise)
	eqn = models.ForeignKey(Equation)
	def __unicode__(self):
		return self.exc.title + " : " +  self.eqn.name

#Link exercises and symbols
class ExcSym(models.Model):
	exc = models.ForeignKey(Exercise)
	symbol = models.ForeignKey(Symbol)
	type = models.IntegerField() #0 is given, 1 is hidden, 2 is find
	def __unicode__(self):
		return self.exc.title + " : " +  self.symbol.symbol