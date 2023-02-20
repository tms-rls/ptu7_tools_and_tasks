
from .models import TaskComment
from django import forms


class TaskCommentForm(forms.ModelForm):
    class Meta:
        model = TaskComment
        fields = ('text', 'employee',)
        widgets = {'task': forms.HiddenInput(), 'employee': forms.HiddenInput()}
