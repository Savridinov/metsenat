from django.urls import path
from students.views import StudentCreateAPIView


urlpatterns = [
    path('create', StudentCreateAPIView.as_view(), name='student-create'),
]