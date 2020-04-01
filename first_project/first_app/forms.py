from django import forms
from django.core import validators
from first_app.models import Users

class NewUserFormName(forms.ModelForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    verify_email = forms.CharField(label='Enter your email again:')

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")

    class Meta:
        model = Users
        fields = '__all__'
