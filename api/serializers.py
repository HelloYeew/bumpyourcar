from django.contrib.auth.models import User
from rest_framework import serializers
from emergency.models import Location, Car
from users.models import Profile


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['lat', 'lng']


class CarStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['has_accident', 'has_drowned']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class CarFullSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Car
        fields = ['id', 'name', 'has_accident', 'has_drowned', 'user']


class EmergencyListSerializer(serializers.Serializer):
    user = UserSerializer()

    class Meta:
        model = Car
        fields = ['name', 'has_accident', 'has_accident', 'user']
        depth = 1
