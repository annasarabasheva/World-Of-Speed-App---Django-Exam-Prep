from django import forms

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileCreateForm(ProfileBaseForm):
    pass
