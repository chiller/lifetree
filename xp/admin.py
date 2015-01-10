from django.contrib import admin
from xp.models import TimeLog, Activity, BadgeType

class TimeLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'activity', 'notes', 'minutes']

admin.site.register(Activity)
admin.site.register(TimeLog, TimeLogAdmin)
admin.site.register(BadgeType)