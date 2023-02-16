import django_filters.rest_framework
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import Sponsors
from .serializers import SponsorsSerializer
# from db.paginations import DefaultPagination


class SponsorsViewSet(ModelViewSet):
    queryset = Sponsors.objects.all()
    serializer_class = SponsorsSerializer
    permission_classes = [IsAdminUser]
    # pagination_class = [DefaultPagination]
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    filterset_fields = ('gender', 'status', 'reg_date', 'sponsorship_amount')




