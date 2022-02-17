from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import PostLocationSerializer
from emergency.models import Location


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def update_user_location(request,user_id):
    """
    API view for POST request to post the location from geolocation API to the database.

    To make sure that the user is authenticated, we use the IsAuthenticated permission class.

    :param request:
    :param user_id: Target user ID
    :return:
    """
    try:
        location = Location.objects.get(user=user_id)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = PostLocationSerializer(location, data=request.data)
        if serializer.is_valid():
            # serializer.validated_data['lat'] = serializer.data['lat']
            # serializer.validated_data['lng'] = serializer.data['lng']
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
