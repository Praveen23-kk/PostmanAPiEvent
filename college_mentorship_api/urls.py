# college_mentorship_api/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('networking.urls')),  # Ensure you have 'api/' prefix here
]
