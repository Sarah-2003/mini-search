from django import forms
from .models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'location', 'phone_number', 'bio', 'profile_photo', 'semester', 'branch']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.RadioSelect(choices=[('male', 'Male'), ('female', 'Female'), ('non-binary', 'Non-binary'), ('prefer_not_to_say', 'Prefer not to say')]),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['profile_photo'].widget.attrs.update({'class': 'form-control-file'})