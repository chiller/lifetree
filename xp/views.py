from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render


from xp.models import TimeLog

def xp(request):
    return TimeLog.objects.filter(user=request.user).aggregate(Sum('minutes'))['minutes__sum']


def level(xpamt):
    level = int((xpamt/100.0)**0.5) + 1
    lower = (level - 1) ** 2 * 100
    upper = level ** 2 * 100
    pct = int((xpamt - lower)*1.0 / (upper - lower) * 10)
    return "".join(map(str,(["Level", level, " Xp ",xpamt, "<br/>", lower, "*"*pct+'.'*(10-pct) ,upper])))

@login_required(login_url="/admin")
def xpview(request):
    logs = TimeLog.get_daily(request.user)
    avg_time = xp(request) / (len(logs) or 1)
    context = {
        'xp': level(xp(request)),
        'logs': TimeLog.get_daily(request.user),
        'avg': avg_time
    }
    return render(request, 'index.html', context)

#TODO: frp on frontend - baconjs
#TODO: http://baconjs.blogspot.fi/2013/02/chicken-egg-and-baconjs.html
#TODO: maybe not
