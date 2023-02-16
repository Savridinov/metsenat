from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SponsorsViewSet

router = DefaultRouter()
router.register('sponsor', SponsorsViewSet)
urlpatterns = [
    path('', include(router.urls))
]
