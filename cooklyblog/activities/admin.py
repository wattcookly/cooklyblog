from django.contrib import admin
from activities.models import Activity, Session

# Register your models here.


class ActivityAdmin(admin.ModelAdmin):
    pass


class SessionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Session, SessionAdmin)
