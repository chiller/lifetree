from django.contrib import admin
from xp.models import TimeLog, Activity, BadgeType

admin.site.register(Activity)
admin.site.register(TimeLog)
admin.site.register(BadgeType)