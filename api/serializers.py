from rest_framework import serializers
from emergency.models import Location


class PostLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['lat', 'lng']