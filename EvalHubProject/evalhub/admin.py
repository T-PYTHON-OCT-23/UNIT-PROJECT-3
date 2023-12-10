from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'manager', 'employee', 'due_date', 'completed')
    list_filter = ('completed', 'due_date')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('task', 'submitted_by', 'submitted_at')
    readonly_fields = ('submitted_by', 'submitted_at')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('task', 'manager', 'completion_status', 'due_date_extension')
    readonly_fields = ('task', 'manager')

admin.site.register(Task, TaskAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Feedback, FeedbackAdmin)
