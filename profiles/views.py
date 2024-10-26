from django.db.models import Sum
from django.shortcuts import render, redirect

from cars.models import Car
from profiles.forms import ProfileCreateForm, ProfileEditForm
from profiles.models import Profile


def create_profile(request):
    profile = Profile.objects.first()
    form = ProfileCreateForm(request.POST or None)

    if profile:
        return redirect('home')

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        "profile": profile,
        "form": form
    }

    return render(request, 'profiles/profile-create.html', context)


def detailed_profile(request):
    profile = Profile.objects.first()
    total_price = Car.objects.filter(owner=profile).aggregate(total=Sum('price'))['total']
    total_price = total_price if total_price is not None else 0.0

    if not profile:
        return redirect('home')

    context = {
        "profile": profile,
        "total_price": total_price
    }

    return render(request, 'profiles/profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    if not profile:
        return redirect('home')

    form = ProfileEditForm(request.POST or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('detailed-profile')

    context = {
        "profile": profile,
        "form": form
    }
    return render(request, 'profiles/profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if not profile:
        return redirect('home')

    if request.method == 'POST':
        profile.delete()
        return redirect('home')

    context = {
        "profile": profile,
    }
    return render(request, 'profiles/profile-delete.html', context)
