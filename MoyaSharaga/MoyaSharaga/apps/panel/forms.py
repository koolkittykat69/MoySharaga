from django import forms

from .models import Timetable

# form for timetable
class TimetableForm(forms.ModelForm):

    class Meta:
        model = Timetable
        fields = ('group', 'subject', 'day', 'subject_datetime_start', 'subject_datetime_stop',)
