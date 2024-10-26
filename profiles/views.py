from django.shortcuts import render, redirect

from profiles.forms import ProfileCreateForm
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