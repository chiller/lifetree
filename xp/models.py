from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class TimeLog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    activity = models.ForeignKey(Activity)
    notes = models.TextField()
    minutes = models.IntegerField(default=0)