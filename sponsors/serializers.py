from rest_framework import serializers
from sponsors.models import Sponsors


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsors
        fields = '__all__'

    def validate(self, attrs):
        if attrs['is_organisation'] == True and attrs['gender'] is not None:
            raise serializers.ValidationError()

