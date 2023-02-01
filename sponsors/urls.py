from django.urls import path
from .views import SponsorCreateAPIView

urlpatterns = [
    path('create', SponsorCreateAPIView.as_view(), name='sponsor-create'),
]