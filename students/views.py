from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import StudentsSerializer


class StudentCreateAPIView(CreateAPIView):
    serializer_class = StudentsSerializer
    permission_classes = [AllowAny]
