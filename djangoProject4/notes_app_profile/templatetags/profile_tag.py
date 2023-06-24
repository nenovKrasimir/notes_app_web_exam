from django import template

from djangoProject4.notes_app_profile import models

register = template.Library()


@register.simple_tag
def get_profile():
    return models.NotesAppProfile.objects.first()

@register.simple_tag
def get_notes():
    return models.NotesAppNote.objects.all()