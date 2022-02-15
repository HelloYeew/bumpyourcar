from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        return redirect('drive')
    return render(request, 'emergency/home.html')


def drive(request):
    parameter = {
        'user': request.user,
    }
    return render(request, 'emergency/drive.html', parameter)