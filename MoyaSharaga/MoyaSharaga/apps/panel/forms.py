from django import forms

from .models import Timetable

class TimetableForm(forms.ModelForm):

    class Meta:
        model = Timetable
        fields = ('group', 'subject', 'day', 'subject_datetime_start', 'subject_datetime_stop',)