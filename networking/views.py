from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from django.shortcuts import render
from django.http import JsonResponse
from .models import Student  # Import your Student model if needed
from .serializers import StudentSerializer,MentorshipRequestSerializer  # Import your serializer if needed


# Additional views like index, welcome, etc.
def index(request):
    return render(request, 'index.html')

def welcome(request):
    return JsonResponse({"message": "Welcome to the College Networking and Mentorship API!"})

# Example view to list mentors
class MentorListView(APIView):
    def get(self, request):
        data = [
            {"id": 1, "name": "John Doe", "expertise": "Data Science"},
            {"id": 2, "name": "Jane Smith", "expertise": "Web Development"},
            {"id": 3, "name": "laxman", "expertise": "AI"},
            {"id": 4, "name": "leela", "expertise": "backend"},
            {"id": 5, "name": "vaishnavi", "expertise": "frontend"},
            {"id": 6, "name": "Praveen", "expertise": "Blockchain"},
            
        ]
        return Response(data, status=status.HTTP_200_OK)
# Example view to create mentorship request
class CreateMentorshipRequestView(APIView):
    def post(self, request):
        request_data = request.data
        # Just return the posted data for testing purposes
        return Response({"message": "Mentorship request created", "data": request_data}, status=status.HTTP_201_CREATED)

# Example view to get user's mentorship requests
class MyMentorshipRequestsView(APIView):
    def get(self, request):
        data = [
            {"id": 1, "mentor": "John Doe", "status": "Pending"},
            {"id": 2, "mentor": "Jane Smith", "status": "Approved"},
        ]
        return Response(data, status=status.HTTP_200_OK)


class CreateMentorshipRequestView(APIView):
    def post(self, request):
        serializer = MentorshipRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the mentorship request
            return Response({"message": "Mentorship request created", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# View to handle student data
class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer