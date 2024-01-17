from django import forms
from .models import Story, Task, TimeEntry, Developer


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'estimated_hours']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'status', 'estimated_hours']

    status = forms.CharField(initial="To Do", widget=forms.HiddenInput())


class TimeEntryForm(forms.ModelForm):
    developer = forms.ModelChoiceField(queryset=Developer.objects.all(), empty_label="Select a Developer")
    status = forms.ChoiceField(choices=Task.status_choices, required=False)  # Make status optional

    class Meta:
        model = TimeEntry
        fields = ['hours_spent', 'description', 'developer', 'status']

    def __init__(self, *args, **kwargs):
        task = kwargs.pop('task', None)  # Remove task from kwargs
        super(TimeEntryForm, self).__init__(*args, **kwargs)
        self.fields['developer'].queryset = Developer.objects.all()
        if task:
            self.instance.task = task

    def save(self, commit=True):
        time_entry = super(TimeEntryForm, self).save(commit=False)
        if commit:
            time_entry.save()
            if time_entry.task:
                time_entry.task.status = self.cleaned_data['status']
                time_entry.task.save()
        return time_entry

