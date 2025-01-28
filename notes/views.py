from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Note
from .forms import NoteForm


def root(request):
    return render(request, "notes/root.html")


class NoteListView(View):
    def get(self, request):
        notes = Note.objects.all()
        return render(request, "notes/note_list.html", {"notes": notes})

    def post(self, request):
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
        return render(request, "notes/note_form.html", {"form": form})


class NoteDetailView(View):
    def get(self, request, id):
        note = get_object_or_404(Note, id=id)
        return render(request, "notes/note_detail.html", {"note": note})

    def post(self, request, id):
        if request.POST.get("_method") == "DELETE":
            note = get_object_or_404(Note, id=id)
            note.delete()
            return redirect("note_list")


class NoteCreateView(View):
    def get(self, request):
        form = NoteForm()
        return render(request, "notes/note_form.html", {"form": form})

    def post(self, request):
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")
        return render(request, "notes/note_form.html", {"form": form})


class NoteEditView(View):
    def get(self, request, id):
        note = get_object_or_404(Note, id=id)
        form = NoteForm(instance=note)
        return render(request, "notes/note_form.html", {"form": form, "note": note})

    def post(self, request, id):
        note = get_object_or_404(Note, id=id)
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_detail", id=note.id)
        return render(request, "notes/note_form.html", {"form": form, "note": note})
