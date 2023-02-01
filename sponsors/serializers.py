from rest_framework import serializers
from sponsors.models import Sponsors


class SponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsors
        fields = '__all__'

    def validate(self, attrs):
        if attrs['is_organisation'] is True and attrs['gender'] is not None:
            raise serializers.ValidationError('Gender or Organisation field required')

