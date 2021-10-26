from django.shortcuts import render

from app.permissions import IsAdminOrReadOnly
from .models import Profile, Subject, Notes

# api
from django.http import JsonResponse
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import SubjectSerializer, NotesSerializer, ProfileSerializer
from .permissions import IsAdminOrReadOnly


# Create your views here.

def index(request):
    return render(request, 'index.html')


# rest api ====================================
class SubjectList(APIView):  # get all Subjects
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):  # get all Subjects
        all_Subjects = Subject.objects.all()
        serializers = SubjectSerializer(all_Subjects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):  # create new Subject
        serializers = SubjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectDetail(APIView):  # get, update, delete single Subject
    permission_classes = (IsAdminOrReadOnly,)

    def get_object(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):  # get Subject
        subject = self.get_object(pk)
        serializers = SubjectSerializer(subject)
        return Response(serializers.data)

    def put(self, request, pk, format=None):  # update Subject
        subject = self.get_object(pk)
        serializers = SubjectSerializer(subject, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):  # delete Subject
        subject = self.get_object(pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NotesList(APIView):  # get all notes
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None): # get all notes
        all_notes = Notes.objects.all()
        serializers = NotesSerializer(all_notes, many=True)
        return Response(serializers.data)

    
    def post(self, request, format=None): # create new note
        serializers = NotesSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class NotesDetail(APIView):  # get, update, delete single note
    permission_classes = (IsAdminOrReadOnly,)

    def get_object(self, pk):
        try:
            return Notes.objects.get(pk=pk)
        except Notes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None): # get note
        notes = self.get_object(pk)
        serializers = NotesSerializer(notes)
        return Response(serializers.data)

    def put(self, request, pk, format=None): # update note
        notes = self.get_object(pk)
        serializers = NotesSerializer(notes, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None): # delete note
        notes = self.get_object(pk)
        notes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ProfileList
class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)
