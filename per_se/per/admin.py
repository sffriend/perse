from django.contrib import admin

# Register your models here.
from per.models import Symbol, Equation, SymbolEquation, Exercise, Tag, Section, SectionEqn, SectionSym, TagLink, ExcEqn, ExcSym

class SymEqChoice(admin.TabularInline):
	model = SymbolEquation
	extra = 2

class SymbolAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,  {'fields': ['symbol']}),
		('Symbol name', {'fields': ['name']}),
		('Constant', {'fields': ['constant']}),
	]
	list_display = ( 'symbol', 'name' ,'constant')
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

class SecSym(admin.TabularInline):
	model = SectionSym
	extra = 2

class SecEqn(admin.TabularInline):
	model = SectionEqn
	extra = 2

class SectionAdmin(admin.ModelAdmin):
	fieldsets = [
		('Chapter Number', {'fields': ['ch_num']}),
        ('name', {'fields': ['name']}),
    ]
	list_display = ( 'ch_num', 'name' )
	list_filter = ['ch_num']
	search_fields = ['name']
	inlines = [SecSym, SecEqn]

class ExcEqnChoice(admin.TabularInline):
	model = ExcEqn
	extra = 2

class ExcSymChoice(admin.TabularInline):
	model = ExcSym
	extra = 2

class ExcTag(admin.TabularInline):
	model = TagLink
	extra = 2

class ExerciseAdmin(admin.ModelAdmin):
	list_display = ( 'sec', 'title' )
	inlines = [ExcEqnChoice, ExcSymChoice, ExcTag]
    
'''
class SymbolAdmin(admin.ModelAdmin):
	fields = ['symbol','name']
'''
admin.site.register(Symbol, SymbolAdmin)
admin.site.register(Equation, EquationAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Tag)
admin.site.register(Section, SectionAdmin)
#admin.site.register(SymbolEquation)