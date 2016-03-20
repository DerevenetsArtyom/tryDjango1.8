from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    # def CLEAN_fieldName
    def clean_email(self):
        ''' Custom func for validating email field '''
        email = self.cleaned_data.get('email')
        if 'edu' not in email:
            raise forms.ValidationError('Please use a valid .EDU email')
        return email


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=200, required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=255)
