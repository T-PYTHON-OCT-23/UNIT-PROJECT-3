from django.contrib import admin
from .models import CustomUser, Task, Report, Feedback

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'role',)
    search_fields = ('user__username', 'role',)

admin.site.register(CustomUser, CustomUserAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'manager', 'employee', 'due_date', 'completed',)
    list_filter = ('completed', 'due_date',)
    search_fields = ('title', 'manager__user__username', 'employee__user__username',)

admin.site.register(Task, TaskAdmin)

class ReportAdmin(admin.ModelAdmin):
    list_display = ('task', 'submitted_by', 'submitted_at',)
    search_fields = ('task__title', 'submitted_by__user__username',)

admin.site.register(Report, ReportAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('task', 'manager', 'completion_status',)
    list_filter = ('completion_status',)
    search_fields = ('task__title', 'manager__user__username',)

admin.site.register(Feedback, FeedbackAdmin)
