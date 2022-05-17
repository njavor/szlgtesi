import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .models import Alkalom, Foglalkozas

@login_required
def indexview(request):
    context = {}
    try:
        filter = Foglalkozas.objects.get(edzo = request.user)
        return HttpResponseRedirect(filter.url + '/')
    except:
        context['foglalkozasok'] = Foglalkozas.objects.all()
        return render(request, "index.html", context)

@login_required
def foglalkozasview(request, fog):
    context = {'alkalmak': Alkalom.objects.filter(foglalkozas__url = fog).order_by('-datum')}
    if not request.user.is_staff:
        try:
            ma = Alkalom.objects.filter(foglalkozas__url = fog).get(datum=datetime.datetime.now())
            context['alkalmak'] = Alkalom.objects.filter(foglalkozas__url = fog).exclude(datum = ma.datum).exclude(datum__gt = ma.datum).order_by('-datum')
            context['ma'] = ma
        except:
            context['alkalmak'] = Alkalom.objects.filter(foglalkozas__url = fog).exclude(datum__gt=datetime.datetime.now()).order_by('-datum')
    else:
        context['staff'] = True
    return render(request, "foglalkozas.html", context)
    

@login_required
def alkalomview(request, fog, alk):
    context = {
        'azalkalom': Alkalom.objects.filter(foglalkozas__url = fog).get(pk = alk),
        'resztvevok': Foglalkozas.objects.get(url = fog).diakok.all(),
    }
    if request.user.is_staff:
        context['staff'] = True
    return render(request, "alkalom.html", context)

