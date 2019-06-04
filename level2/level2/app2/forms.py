from django import forms
from django.core import validators
from app2.models import User


def check_for_a(value):
    if value[0].lower() != 'a':
        raise forms.ValidationError("Should start with A")


class TestForm(forms.Form):
    name = forms.CharField(validators=[check_for_a])
    email = forms.EmailField()
    vemail = forms.EmailField(label="verify email")
    text = forms.CharField(widget=forms.Textarea)
    botctcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
    def clean(self):
        all_clean = super().clean()
        name = all_clean['name']
        email = all_clean['email']
        text = all_clean['text']
        vemail = all_clean['vemail']
        if email != vemail:
            raise forms.ValidationError("MATCH EMAIL")
            return
        print(name)
        print(email)
        print(text)

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = "__all__"
        
