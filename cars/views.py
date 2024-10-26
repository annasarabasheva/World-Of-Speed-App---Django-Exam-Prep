from django.shortcuts import render

from profiles.models import Profile


def catalogue(request):
    profile = Profile.objects.first()
    context = {
        "profile": profile,
    }

    return render(request, 'cars/catalogue.html', context)