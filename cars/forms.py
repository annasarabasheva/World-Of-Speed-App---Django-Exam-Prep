from django import forms

from cars.models import Car


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner', )


class CarCreateForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add a placeholder for the image_url field
        self.fields['image_url'].widget.attrs['placeholder'] = "https://..."