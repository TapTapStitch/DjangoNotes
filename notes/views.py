from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Note
from .forms import NoteForm


def root(request):
    return render(request, "notes/root.html")


class NoteListView(ListView):
    model = Note
    template_name = "notes/note_list.html"
    context_object_name = "notes"


class NoteDetailView(DetailView):
    model = Note
    template_name = "notes/note_detail.html"
    context_object_name = "note"


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"
    success_url = "/notes/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteEditView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"
    context_object_name = "note"
    success_url = "/notes/"

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = '/notes/'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            redirect('/notes/')
        return obj
