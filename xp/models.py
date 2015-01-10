from django.contrib.auth.models import User
from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class TimeLog(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    activity = models.ForeignKey(Activity)
    notes = models.TextField()
    minutes = models.IntegerField(default=0)

# class Badge(models.Model):
#     activity = models.ForeignKey(Activity)
#     level = models.CharField(choices=(
#         ('wood', 'wood'),
#         ('bronze', 'bronze'),
#         ('silver', 'silver'),
#     ))