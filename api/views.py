from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.http import JsonResponse
from emergency.models import Location, Car


@api_view(['GET','PUT'])
def user_location(request, user_id):
    """
    API view for PUT request to post the location from geolocation API to the database or GET request to get the
    location of the user.

    :param request: HTTP request
    :param user_id: Target user ID
    :return: API response
    """
    try:
        location = Location.objects.get(user=user_id)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LocationSerializer(location)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def car_status(request, car_id):
    """
    API view for PUT request to update or GET request to get the status of the car.

    :param request: HTTP request
    :param car_id: Target car ID
    :return: API response
    """
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarStatusSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CarStatusSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_profile(request, user_id):
    """
    API view for GET request to get the profile of the user.

    :param request: HTTP request
    :param user_id: Target user ID
    :return: API response
    """
    try:
        profile = Profile.objects.get(id=user_id)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProfileSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_car(request, car_id):
    """
    API view for GET request to get the full car information from car ID.

    :param request: HTTP request
    :param user_id: Target user ID
    :return: API response
    """
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CarFullSerializer(car)
    return Response(serializer.data, status=status.HTTP_200_OK)


def get_emergency_count(request):
    """
    API view for GET request to get the count of the emergency.

    :param request: HTTP request
    :return: API response
    """
    return JsonResponse({'count': Car.objects.filter(Q(has_accident=True) | Q(has_drowned=True)).filter(~Q(user=None)).count()})


@api_view(['GET'])
def get_emergency_list(request):
    """
    API view for GET request to get the list of the emergency.

    :param request: HTTP request
    :return: API response
    """
    car_list = Car.objects.filter(Q(has_accident=True) | Q(has_drowned=True)).filter(~Q(user=None))
    serializer = CarFullSerializer(car_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)