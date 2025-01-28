from django.urls import path
from .views import root, NoteListView, NoteDetailView, NoteCreateView, NoteEditView

urlpatterns = [
    path("", root, name="root"),
    path("notes/", NoteListView.as_view(), name="note_list"),
    path("notes/new/", NoteCreateView.as_view(), name="note_new"),
    path("notes/<int:id>/", NoteDetailView.as_view(), name="note_detail"),
    path("notes/<int:id>/edit/", NoteEditView.as_view(), name="note_edit"),
]
