from django.shortcuts import render, get_object_or_404
from itertools import chain
from collections import defaultdict
from django.http import HttpResponse
from django.template import RequestContext, loader
from per.models import Symbol, Equation, SymbolEquation, Exercise, Tag, Section, SectionEqn, SectionSym, TagLink, ExcEqn, ExcSym, SectionExc
import json
# Create your views here.

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
    symbol_list = Symbol.objects.order_by('name')
    context = {'symbol_list': symbol_list}
    return render(request, 'per/symbols.html', context)
	
def equations(request):
    eqn_list = Equation.objects.order_by('name')
    context = {'eqn_list': eqn_list}
    return render(request, 'per/equations.html', context)

def sections(request):
    sec_list = Section.objects.order_by('ch_num')
    context = {'sec_list': sec_list}
    return render(request, 'per/sections.html', context)

def exercises(request):
    exc_list = Exercise.objects.order_by('title')
    context = {'exc_list': exc_list}
    return render(request, 'per/exercises.html', context)

def symDetail(request, per_id):
	symbol = get_object_or_404(Symbol, pk=per_id)
	link_list = SymbolEquation.objects.order_by('id')
	the_list = [link_list, symbol]
	context = {'the_list' : the_list}
	return render(request, 'per/symDetail.html', context)
	
def eqnDetail(request, per_id):
	equation = get_object_or_404(Equation, pk=per_id)
	link_list = SymbolEquation.objects.order_by('id')
	exclist = ExcEqn.objects.order_by('id')
	the_list = [link_list, equation, exclist]
	context = {'the_list' : the_list}
	return render(request, 'per/eqnDetail.html', context)

def secDetail(request, per_id):
	section = get_object_or_404(Section, pk=per_id)
	eqn_list = SectionEqn.objects.order_by('id')
	exc_list = Exercise.objects.order_by('title')
	the_list = [eqn_list, section, exc_list]
	context = {'the_list' : the_list}
	return render(request, 'per/secDetail.html', context)

def excDetail(request, per_id):
	exc = get_object_or_404(Exercise, pk=per_id)
	link_list = ExcEqn.objects.order_by('id')
	symbols = ExcSym.objects.order_by('id')
	the_list = [link_list, exc, symbols]
	context = {'the_list' : the_list}
	return render(request, 'per/excDetail.html', context)

def exclist(request):
    exc_list = Exercise.objects.order_by('title')
    link_list = ExcEqn.objects.order_by('id')
    symbols = ExcSym.objects.order_by('id')
    the_list = [link_list, exc_list, symbols]
    context = {'the_list' : the_list}
    return render(request, 'per/testeqn.html', context)

def SecExc(request):
	idlist = request.POST.getlist('choice[]')
	exercises = Exercise.objects.order_by('title')
	exc_list = [] 
	for exc in exercises:
		if str(exc.sec.id) in idlist:
			exc_list.append(exc)
	the_list = [idlist, exc_list]
	context = {'the_list' : the_list}
	return render(request, 'per/testeqn.html', context)

def listResults(request):
	exclist = []
	idlist = request.POST.getlist('choice[]')
	for id in idlist:
		exclist.append(get_object_or_404(Exercise, pk=id))
	link_list = ExcEqn.objects.order_by('id')
	symbols = ExcSym.objects.order_by('id')
	sym_dict = {}
	for sym in symbols:
		if str(sym.exc.id) in idlist:
			if sym.symbol not in sym_dict:
				sym_dict[sym.symbol] = [0, 0, 0]
			if sym.type == 0:
				sym_dict[sym.symbol][0] += 1
			elif sym.type == 1:
				sym_dict[sym.symbol][1] += 1
			elif sym.type == 2:
				sym_dict[sym.symbol][2] += 1
	the_list = [link_list, exclist, symbols, sym_dict]
	context = {'the_list' : the_list}
	return render(request, 'per/excListResults.html', context)

def hair(request):
	return render(request, 'per/hair.html')