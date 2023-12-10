from django import forms
from .models import Report, Feedback

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['report_text']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['notes', 'completion_status', 'due_date_extension']
