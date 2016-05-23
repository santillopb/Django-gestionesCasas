# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import loader, RequestContext
from django.views import generic
from django.utils import timezone
from .forms import ChatForm, FacturaForm, AnadeNotaForm
from datetime import datetime, date, time, timedelta
from .models import Cases, Persona, Xat, NotaCalendario
from django.contrib.auth.models import User
import calendar
# Create your views here.

def calendar2(request):
    year = date.today().year 
    month = date.today().month
    day = date.today().day
    cad = "{0}-{1}-{2}".format(year,month,day)
    return HttpResponse(cad)

def calendario(request):
    year = date.today().year 
    month = date.today().month
    day = date.today().day
    calendario_mes = calendar.month(year, month)
    return HttpResponse(calendario_mes)
"""
class EntradasDia(generic.DayArchiveView):
    queryset=NotaCalendario.objects.order_by('dateField')
    template_name='polls/entradas_dia.html'
    date_field = 'dateField'
    context_object_name='entradas'
    month_format = '%m'

class EntradasMes(generic.MonthArchiveView):
        '''Entradas por mes'''
        queryset=NotaCalendario.objects.order_by('dateField')
        template_name='polls/entradas_mes.html'
        date_field = 'dateField'
        month_format = '%m'
        context_object_name='entradas'

class  EntradasYear(generic.YearArchiveView):
        '''Entradas por año'''
        queryset=NotaCalendario.objects.order_by('dateField')
        template_name='polls/entradas_anyo.html'
        date_field = 'dateField'
        context_object_name='entradas'
        make_object_list='True'
"""
class BlogView(generic.ListView):
    template_name = 'polls/blog.html'
    context_object_name = 'entradas_list'
    def get_queryset(self):
        """
        Return the last five published questions (not including     those set to be
        published in the future).
        """
        return NotaCalendario.objects.filter(
        dateField__lte=timezone.now()
        ).order_by('-dateField')[:5]

def blog(request, persona_id):
    model = Persona
    persona = Persona.objects.get(pk=persona_id)
    year = date.today().year
    month = date.today().month
    day = date.today().day
    context = {'persona': persona, 'year':year, 'month':month, 'day':day}
    return render(request, 'polls/blog.html', context)
def btc_address(request, persona_id):
    model = Persona
    persona = Persona.objects.get(pk=persona_id)
    context = {'persona': persona}
    return render(request, 'polls/btc_address.html', context)
    
class CasesView(generic.ListView):
    template_name = 'polls/cases.html'
    context_object_name = 'latest_cases_list'
    def get_queryset(self):

        return Cases.objects.filter(
        pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class UsersView(generic.ListView):
    template_name = 'polls/users.html'
    context_object_name = 'latest_users_list'
    
    def get_queryset(self):
        """
        Return the last five published questions (not including     those set to be
        published in the future)."""
        return User.objects.all()
"""
class XatView(generic.ListView):
    template_name = 'polls/xat.html'
    context_object_name = 'xat_list'
    
    def get_queryset(self):
        """"""
        Return the last five published questions (not including     those set to be
        published in the future).
        """"""
        return Xat.objects.all()"""

def xat(request):
    xats = Xat.objects.order_by('-date_sent')[:5]
    year=date.today().year
    month = date.today().month
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            escriu = request.POST['escriu']
            xat = Xat.objects.create(text=escriu, user=request.user)
            xat.save()
    else:
        form = ChatForm()
    context = {'xats': xats, 'year':year, 'month':month, 'form':form}
    return render_to_response('polls/xat.html', context, context_instance=RequestContext(request))
"""class XatDetailView(generic.DetailView):
    model = Xat
    template_name = 'polls/xat_detail.html'
    def get_queryset(self):
        """"""
        Excludes any questions that aren't published yet.
        """"""
        return Xat.objects.all()
"""
class NotaView(generic.ListView):
    template_name = 'polls/enguany.html'
    context_object_name = 'nota_list'
    def get_queryset(self):
        """
        Return the last five published questions (not including     those set to be
        published in the future).
        """
        current_year = timezone.now().year
        return NotaCalendario.objects.filter(dateField__year = current_year)



class UserDetailView(generic.DetailView):
    model = User
    template_name = 'polls/user_detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return User.objects.all()

def casesDetail(request, cases_id):
    model = Cases
    template_name = 'polls/detail.html'
    cases = Cases.objects.get(pk=cases_id)
    context = {'cases':cases}
    return render(request, template_name, context)

def factura(request, persona_id):
    model = Persona
    template_name = 'polls/detail_persona.html'
    persones = Persona.objects.get(pk=persona_id)
    message = ""
    context = {'persones':persones}
    return render(request, template_name, context)

def save_factura(request, persona_id):
    message = ""
    if request.method == 'POST':
        form = FacturaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Image uploaded succesfully!"   
        else:
            message = "Errada en la pujada de l'imatge"   
    else:
        form = FacturaForm()
    persona = Persona.objects.get(pk=persona_id)
    return render(request, 'polls/factura_nova.html', {'form':form, 'message':message, 'persona':persona})

def anade_nota(request, persona_id):
    persona = Persona.objects.get(pk=persona_id)
    message = ""
    if request.method == 'POST':
        form = AnadeNotaForm(request.POST)
        if form.is_valid():
            form.save()   
            message = "Nota enviada correctament"
        else:
            message = "Errada"
    else:
        form = AnadeNotaForm()
    return render(request, 'polls/nota_nova.html', {'form':form, 'persona':persona, 'message':message})

def vote(request, cases_id):
    cases = get_object_or_404(Cases, pk=cases_id)
    try:
        selected_persona = cases.persona_set.get(pk=request.POST['persona'])
    except (KeyError, Persona.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'cases': cases,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_persona.votes += 1
        selected_persona.save()

def nota(request, year):
    try:
        year = date.today().year
        xats = Xat.objects.filter(date_sent__year=year)
    except NotaCalendario.DoesNotExist:
        raise Http404("Nota does not exist")
    return render(request, 'polls/enguany.html', {'year':year, 'xats': xats})

def calendar_month(request):
    try:
        now = timezone.now()
        xat = Xat.objects.filter(date_sent__month=now.month, date_sent__year=now.year)
    except NotaCalendario.DoesNotExist:
        raise Http404("Nota does not exist")
    return redirect('polls:calendar_month_day')

def calendar_month_day(request, year, month):
    try:
        year = datetime.today().year
        month = datetime.today().month
        xats = Xat.objects.filter(date_sent__year=year, date_sent__month=month)
    except NotaCalendario.DoesNotExist:
        raise Http404("Nota does not exist")
    return render(request, 'polls/calendar_month.html', {'year':year, 'month': month, 'xats': xats})

def year(request, year):
    try:
        now = timezone.now()
        entradas_list = NotaCalendario.objects.filter(dateField__year=year)
    except NotaCalendario.DoesNotExist:
        raise Http404("Nota does not exist")
    return render(request, 'polls/entradas_anyo.html', {'year':now.year, 'entradas_list': entradas_list})
    
def iframe(request):
    try:
        year = datetime.today().year
        month = datetime.today().month
        xats = Xat.objects.filter(date_sent__year=year)
    except NotaCalendario.DoesNotExist:
        raise Http404("Xat does not exist")
    return render(request, 'polls/iframe.html', {'year':year, 'month':month, 'xats': xats})

def save_chat(request):
    #Xat.objects.create()
    # usuario: request.user
    # texto
    # - fecha
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            escriu = request.POST['escriu']
            xat = Xat.objects.create(text=escriu, user=request.user)
            xat.save()
            
    return redirect('polls:xat')


