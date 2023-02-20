
from .models import ConstructionObjectComment, TaskComment, ToolComment
from django import forms


class TaskCommentForm(forms.ModelForm):
    class Meta:
        model = TaskComment
        fields = ('text', 'employee',)
        widgets = {'task': forms.HiddenInput(), 'employee': forms.HiddenInput()}


class ToolCommentForm(forms.ModelForm):
    class Meta:
        model = ToolComment
        fields = ('text', 'employee',)
        widgets = {'tool': forms.HiddenInput(), 'employee': forms.HiddenInput()}


class ConstructionObjectCommentForm(forms.ModelForm):
    class Meta:
        model = ConstructionObjectComment
        fields = ('text', 'employee',)
        widgets = {'construction_object': forms.HiddenInput(), 'employee': forms.HiddenInput()}
