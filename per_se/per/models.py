from django.db import models

# models

"""
Symbol model containing:
id - an int (by default, not shown here, added automatically)
symbol - a charfield for the symbol LaTeX
name - a charfield for the name of the symbol
constant - a boolean determining whether or not it's a constant
Meta class orders it by name when displayed in the admin page
__unicode__(self) is what is displayed in the admin page, in this case name:symbol
"""
class Symbol(models.Model):
    symbol = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    constant = models.BooleanField(default=False)
    class Meta:
    	ordering = ('name',)
    def __unicode__(self):
    	return self.name + " : " + self.symbol

"""
Equation model containing:
id - an int (by default, not shown here, added automatically)
latex - a charfield for the equation LaTeX
name - a charfield for the name of the equation, should be section-number
Meta class orders it by name when displayed in the admin page
__unicode__(self) is what is displayed in the admin page, in this case name
"""
class Equation(models.Model):
    latex = models.CharField(max_length=500)
    name = models.CharField(max_length=150)
    class Meta:
    	ordering = ('name',)
    def __unicode__(self):
    	return self.name

"""
Section model containing:
id - an int (by default, not shown here, added automatically)
name - a charfield for the name of the equation, should be section-number
ch_num - intfield, chapter number
Meta class orders it by chapter number when displayed in the admin page
__unicode__(self) is what is displayed in the admin page, in this case name
"""
class Section(models.Model):
	name = models.CharField(max_length=100)
	ch_num = models.IntegerField()
	class Meta:
		ordering = ('ch_num',)
	def __unicode__(self):
		return self.name

"""
Exercise model containing:
id - an int (by default, not shown here, added automatically)
latex - a charfield for the equation LaTeX
name - a charfield for the name of the equation, should be section-number
Meta class orders it by name when displayed in the admin page
__unicode__(self) is what is displayed in the admin page, in this case name
"""
class Exercise(models.Model):
	sec = models.ForeignKey(Section)
	text = models.TextField()
	img = models.CharField(max_length = 100)
	title = models.CharField(max_length = 100)
	conceptual = models.BooleanField(default = False)
	calculus = models.BooleanField(default = False)
	class Meta:
		ordering = ('title',)
	def __unicode__(self):
		return self.title

"""
Image model containing:
id - an int (by default, not shown here, added automatically)
exc - a field for an exercise model that the image is associated with
title - name of he image or something, purely for sorting purposes
Meta class orders it by title when displayed in the admin page
__unicode__(self) is what is displayed in the admin page, in this case title
"""
class Image(models.Model):
	exc = models.ForeignKey(Exercise)
	title = models.CharField(max_length = 100)
	image = models.ImageField(upload_to="per/static/per/images", null=True)
	class Meta:
		ordering = ('title',)
	def __unicode__(self):
		return self.title

"""
Tag model containing:
id - an int (by default, not shown here, added automatically)
name - a charfield for the name of the tag
Meta class orders it by name when displayed in the admin page
__unicode__(self) is what is displayed in the admin page, in this case name
"""
class Tag(models.Model):
	name = models.CharField(max_length=100)
	def __unicode__(self):
		return self.name
		
#Linking Tables
"""Linking tables link two tables of models together, should be fairly self-explanatory"""

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

#Link sections and symbols
class SectionExc(models.Model):
	section = models.ForeignKey(Section)
	exercise = models.ForeignKey(Symbol)
	def __unicode__(self):
		return self.section.name + " : " +  self.exercise.title

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