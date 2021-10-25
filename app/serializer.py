from rest_framework import serializers
from .models import Profile, Subject, Notes


# Subject serializer
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("name", "created_at", "updated_at")


# Notes serializer
class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ("user", "title", "description", "subject", "created_at", "updated_at")


# Profile serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user", "bio", "profile_pic", "contact", "location", "notes", "created_at", "updated_at")