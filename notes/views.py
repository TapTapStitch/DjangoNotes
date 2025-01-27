from django.http import HttpResponse
from django.views import View


def root(request):
    return HttpResponse("Hello, world!")


class NoteListView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class NoteDetailView(View):
    def get(self, request, id):
        # Handle GET request for retrieving a specific note
        pass

    def put(self, request, id):
        # Handle PUT request to update a specific note
        pass

    def patch(self, request, id):
        # Handle PATCH request to partially update a specific note
        pass

    def delete(self, request, id):
        # Handle DELETE request to delete a specific note
        pass
