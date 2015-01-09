from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from xp.models import TimeLog

trees = ["lifetree", "coursera", "euler"]


def xp():
    return TimeLog.objects.aggregate(Sum('minutes'))['minutes__sum']


def level():
    xpamt = xp()
    level = int((xpamt/100.0)**0.5) + 1
    lower = (level - 1) ** 2 * 100
    upper = level ** 2 * 100
    pct = int((xpamt - lower)*1.0 / (upper - lower) * 10)
    return "".join(map(str,(["Level", level, " Xp ",xpamt, "<br/>", lower, "*"*pct+'.'*(10-pct) ,upper])))

def xpview(request):
    return HttpResponse(level())