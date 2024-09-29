# networking/models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class MentorshipRequest(models.Model):
    mentor_id = models.IntegerField()  # Assuming mentor ID is stored as an integer
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request to mentor {self.mentor_id} - {self.message}"