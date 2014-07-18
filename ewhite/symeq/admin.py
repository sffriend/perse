from django.contrib import admin
from symeq.models import Symbol
from symeq.models import Equation
from symeq.models import SymEq

class SymEqChoice(admin.TabularInline):
	model = SymEq
	extra = 2

class SymbolAdmin(admin.ModelAdmin):
	#fields = ['symbol', 'name']
	fieldsets = [
		(None,  {'fields': ['symbol']}),
		('Symbol name', {'fields': ['name']}),
	]
	list_display = ( 'symbol', 'name' )
	list_filter = ['name']
	search_fields = ['name']

#class SymEqAdmin(admin.ModelAdmin):
#	display = ['eq']

class EquationAdmin(admin.ModelAdmin):
        fieldsets = [
                ('LaTeX form',  {'fields': ['equation']}),
                ('Eqn. name', {'fields': ['name']}),
        ]
	inlines = [SymEqChoice]
	list_display = ( 'equation', 'name' )
	search_fields = ['name']

admin.site.register(Symbol, SymbolAdmin)
admin.site.register(Equation, EquationAdmin)
#admin.site.register(SymEq, SymEqAdmin)


# Register your models here.
