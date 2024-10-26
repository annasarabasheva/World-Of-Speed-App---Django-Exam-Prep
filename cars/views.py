from django.shortcuts import render, redirect

from cars.forms import CarCreateForm
from cars.models import Car
from profiles.models import Profile


def catalogue(request):
    cars = Car.objects.all()
    profile = Profile.objects.first()

    if not profile:
        return redirect('home')

    context = {
        "profile": profile,
        "cars": cars
    }

    return render(request, 'cars/catalogue.html', context)


def create_car(request):
    profile = Profile.objects.first()
    if not profile:
        return redirect('home')

    form = CarCreateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = profile
            car.save()
            return redirect('catalogue')

    context = {
        "profile": profile,
        "form": form
    }

    return render(request, 'cars/car-create.html', context)


def detailed_car(request, id):
    car = Car.objects.get(id=id)
    profile = Profile.objects.first()
    if not profile:
        return redirect('home')

    context = {
        "car": car,
        "profile": profile
    }
    return render(request, 'cars/car-details.html',context)