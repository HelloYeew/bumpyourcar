from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Car


def home(request):
    """
    The first place when user access the website. If user is authenticated then redirect to the app.
    :param request: WSGI request from user.
    :return: The home for guest or redirect to the app if user is authenticated.
    """
    if request.user.is_authenticated:
        return redirect('drive')
    return render(request, 'emergency/home.html')


@login_required
def drive(request):
    """
    The main page for the app. This page use to track the user's location when user is driving.
    :param request: WSGI request from user.
    :return: Render the page and pass the value from context to the template (drive.html)
    """
    parameter = {
        'user': request.user,
        'background_image': 'img/fuckinghelpme.png'
    }
    return render(request, 'emergency/drive.html', parameter)


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def staff(request):
    """
    The page for the staff. It's used to manage the accident or emergency and manage the user information too.

    This page is only accessible for the staff and superuser.

    :param request: WSGI request from user.
    :return: Render the page and pass the value from context to the template (staff.html)
    """
    parameter = {
        'user': request.user,
        'background_image': 'img/fuckinghelpme.png',
        'accident_count': Car.objects.filter(has_accident=True).count(),
    }
    return render(request, 'emergency/staff.html', parameter)


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def car_list(request):
    """
    The page for the staff to see all the car information.

    This page is only accessible for the staff and superuser.

    :param request: WSGI request from user.
    :return: Render the page and pass the value from context to the template (car_list.html)
    """
    parameter = {
        'car_list': Car.objects.all().order_by('id'),
        'background_image': 'img/fuckinghelpme.png'
    }
    return render(request, 'emergency/car_list.html', parameter)


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def user_list(request):
    """
    The page for the staff to see all the user information.

    This page is only accessible for the staff and superuser.

    :param request: WSGI request from user.
    :return: Render the page and pass the value from context to the template (user_list.html)
    """
    parameter = {
        'user_list': User.objects.all().order_by('id'),
        'background_image': 'img/fuckinghelpme.png'
    }
    return render(request, 'emergency/user_list.html', parameter)


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def emergency_list(request):
    """
    This page for the staff to list all the emergency.

    This page is only accessible for the staff and superuser.

    :param request: WSGI request from user.
    :return: Render the page and pass the value from context to the template (emergency_list.html)
    """
    parameter = {
        'emergency_list': Car.objects.filter(has_accident=True).order_by('id'),
        'background_image': 'img/fuckinghelpme.png'
    }
    return render(request, 'emergency/emergency_list.html', parameter)


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def emergency_detail(request, car_id):
    """

    :param request:
    :param car_id:
    :return:
    """
    car = Car.objects.get(id=car_id)
    if not car.has_accident:
        messages.error(request, "This car has no accident now!")
        return redirect('emergency_list')
    else:
        parameter = {
            'car': car,
            'user_object': car.user,
            'background_image': 'img/fuckinghelpme.png',
            'location': car.user.location,
        }
        return render(request, 'emergency/emergency_detail.html', parameter)


@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def resolve_car(request, car_id):
    """
    API view for mark the car as resolved.

    :param request:
    :param car_id:
    :return:
    """
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return HttpResponse(status=404)

    if not car.has_accident:
        return HttpResponse(status=400)
    else:
        car.has_accident = False
        car.save()
        messages.success(request, "Resolve succesfully!")
        return redirect('emergency_list')
