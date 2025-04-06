from django.forms import ModelForm, DateTimeInput
from django.contrib.auth.models import User
from .models import Event, Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class EventForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date' : DateTimeInput(attrs={
                'type' : 'datetime-local',
                'class': 'form-control'
            })
        }
        exclude = ['organiser', 'interested']

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        #fields = ['profile_picture', 'bio']
        fields = ['bio']