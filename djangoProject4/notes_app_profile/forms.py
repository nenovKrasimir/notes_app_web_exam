from django import forms
from django.core.exceptions import ValidationError

from .models import NotesAppNote, NotesAppProfile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = NotesAppProfile
        fields = '__all__'


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = NotesAppNote
        fields = '__all__'


class DeleteNoteForm(forms.ModelForm):
    class Meta:
        model = NotesAppNote
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['disabled'] = True
