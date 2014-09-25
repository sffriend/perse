from django.shortcuts import render, get_object_or_404
from itertools import chain
from collections import defaultdict
from django.http import HttpResponse
from django.template import RequestContext, loader
from per.models import Symbol, Equation, SymbolEquation, Exercise, Image, Tag, Section, SectionEqn, SectionSym, TagLink, ExcEqn, ExcSym, SectionExc
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

#main index page
def index(request):
	return render(request, 'per/index.html')

#symbols page	
def symbols(request):
    symbol_list = Symbol.objects.order_by('name')
    context = {'symbol_list': symbol_list}
    return render(request, 'per/symbols.html', context)
	
#equations page
def equations(request):
    eqn_list = Equation.objects.order_by('name')
    context = {'eqn_list': eqn_list}
    return render(request, 'per/equations.html', context)

#sections page
def sections(request):
    sec_list = Section.objects.order_by('ch_num')
    context = {'sec_list': sec_list}
    return render(request, 'per/sections.html', context)

#exercises page
def exercises(request):
    exc_list = Exercise.objects.order_by('title')
    context = {'exc_list': exc_list}
    return render(request, 'per/exercises.html', context)

#individual symbol page showing details
def symDetail(request, per_id):
	symbol = get_object_or_404(Symbol, pk=per_id)
	link_list = SymbolEquation.objects.order_by('id')
	the_list = [link_list, symbol]
	context = {'the_list' : the_list}
	return render(request, 'per/symDetail.html', context)

#individual equation page showing details
def eqnDetail(request, per_id):
	equation = get_object_or_404(Equation, pk=per_id)
	link_list = SymbolEquation.objects.order_by('id')
	exclist = ExcEqn.objects.order_by('id')
	the_list = [link_list, equation, exclist]
	context = {'the_list' : the_list}
	return render(request, 'per/eqnDetail.html', context)

#individual section page showing details
def secDetail(request, per_id):
	section = get_object_or_404(Section, pk=per_id)
	eqn_list = SectionEqn.objects.order_by('id')
	exc_list = Exercise.objects.order_by('title')
	the_list = [eqn_list, section, exc_list]
	context = {'the_list' : the_list}
	return render(request, 'per/secDetail.html', context)

#individual exercise page showing details
def excDetail(request, per_id):
	exc = get_object_or_404(Exercise, pk=per_id)
	link_list = ExcEqn.objects.order_by('id')
	symbols = ExcSym.objects.order_by('id')
	images = Image.objects.order_by('id')
	the_list = [link_list, exc, symbols, images]
	context = {'the_list' : the_list}
	return render(request, 'per/excDetail.html', context)

#After selecting sections on the section page, there's a list of exercises, submit will take you to this page
#the for loop sorts the symbols in each exercise by given, hidden, and find and pushes it into a diction corresponding to each exercise
def exclist(request):
    exc_list = Exercise.objects.order_by('title')
    link_list = ExcEqn.objects.order_by('id')
    symbols = ExcSym.objects.order_by('id')
    sym_dict = {}
    for sym in symbols:
		if sym.symbol not in sym_dict:
			sym_dict[sym.symbol] = [0, 0, 0]
		if sym.type == 0:
			sym_dict[sym.symbol][0] += 1
		elif sym.type == 1:
			sym_dict[sym.symbol][1] += 1
		elif sym.type == 2:
			sym_dict[sym.symbol][2] += 1
    the_list = [link_list, exc_list, symbols, sym_dict]
    context = {'the_list' : the_list}
    return render(request, 'per/testeqn.html', context)

#no longer used, it was something I used to make sure selecting exercises and seeing the dashboard output worked
#now it's used for all exercises on the index
def SecExc(request):
	idlist = request.POST.getlist('choice[]')
	exercises = Exercise.objects.order_by('title')
	exc_dict = {}
	for exc in exercises:
		if exc.sec not in exc_dict:
			exc_dict[exc.sec] = []
		exc_dict[exc.sec].append(exc)
	the_list = [idlist, exc_dict]
	context = {'the_list' : the_list}
	return render(request, 'per/SecExcList.html', context)

#the results of selecting exercises, works more or less the same as exclist, except this one takes a pushed list of exercise id numbers for processing
def listResults(request):
	exclist = []
	idlist = request.POST.getlist('choice[]')
	for id in idlist:
		exclist.append(get_object_or_404(Exercise, pk=id))
	link_list = ExcEqn.objects.order_by('id')
	symbols = ExcSym.objects.order_by('id')
	sym_dict = {}
	def getKey(exc):
		return exc.title
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
	the_list = [link_list, sorted(exclist,key=getKey), symbols, sym_dict]
	context = {'the_list' : the_list}
	return render(request, 'per/excListResults.html', context)

def hair(request):
	return render(request, 'per/hair.html')