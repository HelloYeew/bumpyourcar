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
        fields = ['has_accident']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class CarFullSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Car
        fields = ['id', 'name', 'has_accident', 'user']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'image', 'personal_id', 'address']
        depth = 1
