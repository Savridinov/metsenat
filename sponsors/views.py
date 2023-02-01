from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import SponsorsSerializer


class SponsorCreateAPIView(CreateAPIView):
    serializer_class = SponsorsSerializer
    permission_classes = [AllowAny]

