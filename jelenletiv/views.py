from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Alkalom, Foglalkozas

@login_required
def indexview(request):
    context = {}
    try:
        filter = Foglalkozas.objects.get(edzo = request.user)
        context['alkalmak'] = Alkalom.objects.filter(foglalkozas = filter)
    except:
        context['foglalkozasok'] = Foglalkozas.objects.all()

    return render(request, "index.html", context)

@login_required
def alkalomview(request, fog, alk):
    print(fog + " - ez a fog")
    context = {
        'azalkalom': Alkalom.objects.filter(foglalkozas__url = fog).get(pk = alk),
        'resztvevok': Foglalkozas.objects.get(url = fog).diakok.all(),
    }
    return render(request, "alkalom.html", context)