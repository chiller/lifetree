import datetime
from django.contrib.auth.models import User
from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name


class TimeLog(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True, editable=True)
    date.editable = True
    activity = models.ForeignKey(Activity)
    notes = models.TextField()
    minutes = models.IntegerField(default=0)

    @classmethod
    def get_daily(cls, user):
        logs = TimeLog.objects.filter(user=user)
        firstday = logs[0].date.date()
        lastday = datetime.date.today()
        numdays = (lastday - firstday).days

        date_list = [lastday - datetime.timedelta(days=x) for x in range(0, numdays+1)]
        return map(lambda date: [date, logs.filter(date__year=date.year, date__month=date.month, date__day=date.day).count()] ,date_list)




class Badge(models.Model):
    user = models.ForeignKey(User)
    level = models.CharField(choices=(
        ('wood', 'wood'),
        ('bronze', 'bronze'),
        ('silver', 'silver'),
        ('gold', 'gold'),
    ), max_length=20)


class BadgeType(models.Model):
    activity = models.ForeignKey(Activity, null=True)
    name = models.CharField(max_length=30)
    #type = [times tracked, days consecutive tracked, net time tracked]
    #increments = [1,2,5,10]
    #image = models.ImageField()