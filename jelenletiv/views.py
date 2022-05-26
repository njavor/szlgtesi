import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect

from .models import Alkalom, Foglalkozas, Osztaly, Tanulo

@login_required
def indexview(request):
    context = {}
    try:
        filter = Foglalkozas.objects.get(edzo = request.user)
        return HttpResponseRedirect(filter.url + '/')
    except:
        if request.method == "POST":
            data = str(request.POST['data']).split("\n")
            if 'edzo' in request.POST:
                for sor in data:
                    fields = sor.split(",")
                    User.objects.create(
                        username = fields[0],
                        last_name = fields[1],
                        first_name = fields[2],
                        password = make_password(fields[3]),
                    )
            elif 'foglalkozas' in request.POST:
                for sor in data:
                    fields = sor.split(",")
                    Foglalkozas.objects.create(
                        nev = fields[0],
                        url = fields[1],
                        edzo = User.objects.get(username = fields[2]),
                    )
            elif 'tanulo' in request.POST:
                for sor in data:
                    fields = sor.split(",")
                    Osztaly.objects.update_or_create(evfolyam = str(fields[1]), tagozat = str(fields[2]))
                    udiak = Tanulo.objects.create(
                        nev = fields[0],
                        osztaly = Osztaly.objects.get(evfolyam = str(fields[1]), tagozat = str(fields[2])),
                    )
                    Foglalkozas.objects.get(nev = fields[3]).diakok.add(udiak)
            elif 'etorles' in request.POST:
                User.objects.filter(is_staff = False).delete()
            elif 'ftorles' in request.POST:
                Foglalkozas.objects.all().delete()
            elif 'ttorles' in request.POST:
                Tanulo.objects.all().delete()
            elif 'alltorles' in request.POST:
                return HttpResponseRedirect("mindentorles/")

        context['foglalkozasok'] = Foglalkozas.objects.all()
        return render(request, "index.html", context)


@login_required
def alldeleteview(request):
    if request.user.is_staff:
        if request.method == "POST":
            if 'mehet' in request.POST:
                Foglalkozas.objects.all().delete()
                Tanulo.objects.all().delete()
                Alkalom.objects.all().delete()
                User.objects.filter(is_staff = False).delete()
            return HttpResponseRedirect("/")
    else: return HttpResponseRedirect(Foglalkozas.objects.get(edzo = request.user).url + '/')

    return render(request, "alldelete.html", {})



@login_required
def foglalkozasview(request, fog):
    context = {'alkalmak': Alkalom.filterurl(fog).order_by('-datum')}
    if not request.user.is_staff:
        try:
            ma = Alkalom.geturldatum(fog, datetime.datetime.now())
            context['alkalmak'] = Alkalom.filterurl(fog).exclude(datum = ma.datum).exclude(datum__gt = ma.datum).order_by('-datum')
            context['ma'] = ma
        except:
            context['alkalmak'] = Alkalom.filterurl(fog).exclude(datum__gt=datetime.datetime.now()).order_by('-datum')
    else:
        context['staff'] = True
        context['resztvevok'] = Foglalkozas.objects.get(url = fog).diakok.all()
        if request.method == "POST":
            data = str(request.POST['data']).split("\n")
            if 'alkalom' in request.POST:
                for sor in data:
                    fields = sor.split(",")
                    print(fields)
                    Alkalom.objects.create(
                        datum = fields[0],
                        foglalkozas = Foglalkozas.objects.get(url = fog)
                    )
            elif 'atorles' in request.POST:
                Alkalom.objects.all().delete()
    return render(request, "foglalkozas.html", context)
    

@login_required
def alkalomview(request, fog, alk):
    context = {
        'azalkalom': Alkalom.filterurl(fog).get(pk = alk),
        'resztvevok': Foglalkozas.geturl(fog).diakok.all(),
        'hianyzok': Alkalom.filterurl(fog).get(pk = alk).hianyzok.all(),
    }
    if request.user.is_staff:
        context['staff'] = True
    return render(request, "alkalom.html", context)

