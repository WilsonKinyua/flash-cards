from django.shortcuts import render,redirect
from .forms import EntryForm
from app.permissions import IsAdminOrReadOnly
from .models import Subject, Notes

# api
from django.http import JsonResponse
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import SubjectSerializer,NotesSerializer
from .permissions import IsAdminOrReadOnly



# Create your views here.

def index(request):
    return render(request, 'index.html')


# rest api ====================================
class SubjectList(APIView):  # get all Subjects
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_Subjects = Subject.objects.all()
        serializers = SubjectSerializer(all_Subjects, many=True)
        return Response(serializers.data)


class NotesList(APIView):  # get all notes
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_notes = Subject.objects.all()
        serializers = NotesSerializer(all_notes, many=True)
        return Response(serializers.data)

def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EntryForm()

    context = {'form' : form}

    return render(request, 'entries/add.html', context)

def home(request):
    entries = Notes.objects.order_by('-date_posted')
    print('***')
    context = {
        'entries' : entries
    }
   
    return render(request, 'entries/index.html', context)    