from rest_framework import serializers
from .models import *


class SponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsors
        fields = '__all__'


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'