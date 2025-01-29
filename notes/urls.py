from django.urls import path
from .views import (
    root,
    NoteListView,
    NoteDetailView,
    NoteCreateView,
    NoteEditView,
    NoteDeleteView,
)

urlpatterns = [
    path("", root, name="root"),
    path("notes/", NoteListView.as_view(), name="note_list"),
    path("notes/new/", NoteCreateView.as_view(), name="note_new"),
    path("notes/<int:pk>/", NoteDetailView.as_view(), name="note_detail"),
    path("notes/<int:pk>/edit/", NoteEditView.as_view(), name="note_edit"),
    path("notes/<int:pk>/delete/", NoteDeleteView.as_view(), name="note_delete"),
]
