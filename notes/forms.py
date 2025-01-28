from django import forms
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator
from .models import Note


class NoteForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(
                10, message="Title must be at least 10 characters long."
            ),
            MaxLengthValidator(200, message="Title cannot exceed 100 characters."),
        ],
        widget=forms.TextInput(
            attrs={
                "class": "block w-full px-4 py-2 border rounded-md shadow-sm focus:outline-none focus:ring focus:border-blue-300",
                "placeholder": "Enter title",
            }
        ),
        label="Title",
        help_text="Enter the title of the note.",
        error_messages={
            "required": "Please enter a title.",
        },
    )

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "block w-full px-4 py-2 border rounded-md shadow-sm focus:outline-none focus:ring focus:border-blue-300",
                "placeholder": "Enter content",
                "rows": 5,
            }
        ),
        label="Content",
        help_text="Enter the content of the note.",
        error_messages={
            "required": "Please enter content.",
        },
    )

    author = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "block w-full px-4 py-2 border rounded-md shadow-sm focus:outline-none focus:ring focus:border-blue-300",
            }
        ),
        label="Author",
        help_text="Select the author of the note.",
        error_messages={
            "required": "Please select an author.",
        },
    )

    class Meta:
        model = Note
        fields = ["title", "content", "author"]
