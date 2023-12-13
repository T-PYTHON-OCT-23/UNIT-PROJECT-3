from django.contrib import admin
from .models import CustomUser, Task, Report, Feedback

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'manager', 'performance_rating', 'birth_date')
    search_fields = ('user__username', 'user__email')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'manager', 'employee', 'due_date', 'status', 'completed')
    list_filter = ('status', 'completed')
    search_fields = ('title', 'manager__user__username', 'employee__user__username')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('task', 'report_text', 'submitted_by', 'submitted_at')
    search_fields = ('task__title', 'submitted_by__user__username')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('manager', 'task', 'notes', 'completion_status', 'due_date_extension')
    list_filter = ('completion_status',)
    search_fields = ('task__title', 'manager__user__username')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Feedback, FeedbackAdmin)
