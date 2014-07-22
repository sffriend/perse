from django.shortcuts import render, get_object_or_404
from itertools import chain

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

from per.models import Symbol, Equation, SymbolEquation, Exercise, Tag, Section, SectionEqn, SectionSym, TagLink, ExcEqn, ExcSym

'''
def index(request):
    latest_symbol_list = Symbol.objects.order_by('id')
    latest_eqn_list = Equation.objects.order_by('id')
    the_list = [latest_symbol_list, latest_eqn_list]
    context = {'the_list': the_list}
    return render(request, 'per/index.html', context)
'''

def index(request):
	return render(request, 'per/index.html')
	
def symbols(request):
    symbol_list = Symbol.objects.order_by('id')
    context = {'symbol_list': symbol_list}
    return render(request, 'per/symbols.html', context)
	
def equations(request):
    eqn_list = Equation.objects.order_by('id')
    context = {'eqn_list': eqn_list}
    return render(request, 'per/equations.html', context)

def sections(request):
    sec_list = Section.objects.order_by('ch_num')
    context = {'sec_list': sec_list}
    return render(request, 'per/sections.html', context)

def symDetail(request, per_id):
	symbol = get_object_or_404(Symbol, pk=per_id)
	link_list = SymbolEquation.objects.order_by('id')
	the_list = [link_list, symbol]
	context = {'the_list' : the_list}
	return render(request, 'per/symDetail.html', context)
	
def eqnDetail(request, per_id):
	equation = get_object_or_404(Equation, pk=per_id)
	link_list = SymbolEquation.objects.order_by('id')
	the_list = [link_list, equation]
	context = {'the_list' : the_list}
	return render(request, 'per/eqnDetail.html', context)

def secDetail(request, per_id):
	section = get_object_or_404(Section, pk=per_id)
	eqn_list = SectionEqn.objects.order_by('id')
	the_list = [eqn_list, section]
	context = {'the_list' : the_list}
	return render(request, 'per/secDetail.html', context)