
from .models import ConstructionObjectComment, TaskComment, ToolComment, Task
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


class DateInsertion(forms.DateInput):
    input_type = 'datetime-local'


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'employee', 'status']
        widgets = {'deadline': DateInsertion()}
