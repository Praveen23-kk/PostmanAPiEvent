# networking/urls.py

from django.urls import path
from .views import (
    MentorListView,
    CreateMentorshipRequestView,
    MyMentorshipRequestsView,
    StudentListView,
    index,          # Ensure this is imported
    welcome,        # Ensure this is imported
)

urlpatterns = [
    path('', welcome, name='welcome'),  # Optional: serve a welcome message at the root
    path('index/', index, name='index'),  # Ensure this line is present for the index view
    path('mentors/', MentorListView.as_view(), name='mentor-list'),
    path('mentorship-request/', CreateMentorshipRequestView.as_view(), name='create-mentorship-request'),
    path('my-requests/', MyMentorshipRequestsView.as_view(), name='my-mentorship-requests'),
    path('students/', StudentListView.as_view(), name='student-list'),
]
