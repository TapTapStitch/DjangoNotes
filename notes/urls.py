from django.urls import path
from .views import root, NoteListView, NoteDetailView

urlpatterns = [
    path("", root, name="root"),
    path("notes/", NoteListView.as_view()),
    path("notes/<int:id>/", NoteDetailView.as_view()),
]
