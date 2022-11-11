from django.contrib import admin
from .models import Enrollment,Learning_progress,Feedback

admin.site.register(Feedback)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    radio_fields = {"is_paid_subscription": admin.HORIZONTAL}
    
@admin.register(Learning_progress)
class Learning_progressAdmin(admin.ModelAdmin):
    radio_fields = {"status": admin.HORIZONTAL}    