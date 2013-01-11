from django import forms
from homepage.models import EmailRecorder


class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailRecorder
        fields = ('campaign', 'email', 'medium', 'source')