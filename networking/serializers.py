# networking/serializers.py

from rest_framework import serializers
from .models import Student,MentorshipRequest

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class MentorshipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorshipRequest
        fields = ['mentor_id', 'message']