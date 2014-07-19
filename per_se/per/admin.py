from django.contrib import admin

# Register your models here.
from per.models import Symbol, Equation, SymbolEquation

class SymEqChoice(admin.TabularInline):
	model = SymbolEquation
	extra = 2

class SymbolAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,  {'fields': ['symbol']}),
		('Symbol name', {'fields': ['name']}),
	]
	list_display = ( 'symbol', 'name' )
	list_filter = ['name']
	search_fields = ['name']

class EquationAdmin(admin.ModelAdmin):
        fieldsets = [
                ('LaTeX form',  {'fields': ['latex']}),
                ('Eqn. name', {'fields': ['name']}),
        ]
	inlines = [SymEqChoice]
	list_display = ( 'latex', 'name' )
	search_fields = ['name']
'''
class SymbolAdmin(admin.ModelAdmin):
	fields = ['symbol','name']
'''
admin.site.register(Symbol, SymbolAdmin)
admin.site.register(Equation, EquationAdmin)
#admin.site.register(SymbolEquation)