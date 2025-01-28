from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "author"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "block w-full px-4 py-2 border rounded-md shadow-sm focus:outline-none focus:ring focus:border-blue-300",
                    "placeholder": "Enter title",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "block w-full px-4 py-2 border rounded-md shadow-sm focus:outline-none focus:ring focus:border-blue-300",
                    "placeholder": "Enter content",
                    "rows": 5,
                }
            ),
            "author": forms.Select(
                attrs={
                    "class": "block w-full px-4 py-2 border rounded-md shadow-sm focus:outline-none focus:ring focus:border-blue-300",
                }
            ),
        }
        labels = {
            "title": "Title",
            "content": "Content",
            "author": "Author",
        }
        help_texts = {
            "title": "Enter the title of the note.",
            "content": "Enter the content of the note.",
            "author": "Select the author of the note.",
        }
        error_messages = {
            "title": {
                "required": "Please enter a title.",
            },
            "content": {
                "required": "Please enter content.",
            },
            "author": {
                "required": "Please select an author.",
            },
        }
