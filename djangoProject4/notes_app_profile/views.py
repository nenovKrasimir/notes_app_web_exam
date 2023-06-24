from django.shortcuts import render, redirect

from djangoProject4.notes_app_profile.forms import CreateProfileForm, AddNoteForm, DeleteNoteForm
from djangoProject4.notes_app_profile.models import NotesAppNote, NotesAppProfile


def home_page(request):
    form = CreateProfileForm()
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {'form': form}
    return render(request, template_name='home-with-profile.html', context=context)


def check_profile(request):
    notes_count = len(NotesAppNote.objects.all())

    context = {'notes_count': notes_count}
    return render(request, template_name='profile.html', context=context)


def delete_profile(request):
    NotesAppProfile.objects.all().delete()
    NotesAppNote.objects.all().delete()

    return redirect('home-page')


def add_note(request):
    form = AddNoteForm()
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {'form': form}
    return render(request, template_name='note-create.html', context=context)


def edit_note(request, pk):
    note = NotesAppNote.objects.get(id=pk)
    form = AddNoteForm(instance=note)

    if request.method == 'POST':
        form = AddNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {'form': form}
    return render(request, template_name='note-edit.html', context=context)


def delete_note(request, pk):
    note = NotesAppNote.objects.get(id=pk)
    form = DeleteNoteForm(instance=note)

    if request.method == 'POST':
        note.delete()
        return redirect('home-page')

    return render(request, template_name='note-delete.html', context={'form': form})


def details_note(request, pk):
    note = NotesAppNote.objects.get(id=pk)
    context = {'note': note}

    return render(request, template_name='note-details.html', context=context)
