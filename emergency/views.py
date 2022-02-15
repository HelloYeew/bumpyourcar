from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        return redirect('drive')
    return render(request, 'emergency/home.html')


@login_required
def drive(request):
    parameter = {
        'user': request.user,
        'background_image': 'img/943545.jpeg'
    }
    return render(request, 'emergency/drive.html', parameter)