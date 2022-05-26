from django.db import models
from django.contrib.auth.models import User

class Osztaly(models.Model):
    class Meta:
        verbose_name = "Osztály"
        verbose_name_plural = "Osztályok"

    evfolyam = models.CharField(max_length=2)
    tagozat = models.CharField(max_length=1)

    def __str__(self) -> str:
        return self.evfolyam + self.tagozat

class Tanulo(models.Model):
    class Meta:
        verbose_name = "Tanuló"
        verbose_name_plural = "Tanulók"

    nev = models.CharField(max_length=255)
    osztaly = models.ForeignKey(Osztaly, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nev + " - " + str(self.osztaly)



class Foglalkozas(models.Model):
    class Meta:
        verbose_name = "Foglalkozás"
        verbose_name_plural = "Foglalkozások"

    nev = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    edzo = models.ForeignKey(User, on_delete=models.CASCADE)
    diakok = models.ManyToManyField(Tanulo)

    def __str__(self) -> str:
        return self.nev + " - " + self.edzo.last_name + " " + self.edzo.first_name

    def geturl(f):
        return Foglalkozas.objects.get(url = f)


class Alkalom(models.Model):
    class Meta:
        verbose_name = "Alkalom"
        verbose_name_plural = "Alkalmak"

    datum = models.DateField()
    foglalkozas = models.ForeignKey(Foglalkozas, on_delete=models.CASCADE)
    hianyzok = models.ManyToManyField(Tanulo, blank=True)

    def __str__(self) -> str:
        return str(self.datum) + " - " + self.foglalkozas.nev

    def filterurl(f):
        return Alkalom.objects.filter(foglalkozas__url = f)
        
    def geturldatum(f, d):
        return Alkalom.objects.filter(foglalkozas__url = f).get(datum=d)
