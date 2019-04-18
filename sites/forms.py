from django import forms
from django.contrib.auth.models import User
from django.core.validators import ValidationError
from django.contrib.auth.forms import UserCreationForm


def checkEmail(email):
    try:
        User.objects.get(email=email)
        raise ValidationError("User already exist!")
    except User.DoesNotExist:
        pass



def checkLoginEmail(email):
    try:
        User.objects.get(email=email)
        raise ValidationError("Give a valid email! ")
    except User.DoesNotExist:
        pass

class NewSignupForm(UserCreationForm):
    email = forms.EmailField(validators=[checkEmail])
# through class meta we can manage the position of emailfield
    class Meta:
        model = User
        fields = ("username", "email","password1","password2")



class ResetPasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Password',
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Password confirmation',
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput
    )

    def clean(self):
        form_data = self.cleaned_data
        if 'password1' in form_data and 'password2' in form_data:
            if form_data['password1'] != form_data['password2']:
                self.errors['password2'] = ['Enter the same password as before, for verification.']
        return form_data

def checkUsername(username):

    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        raise ValidationError('Invalid user!')


class ForgotPasswordForm(forms.Form):

    username = forms.CharField(max_length=50, validators=[checkUsername])
    email = forms.EmailField()


class LoginForm(forms.Form):

    username = forms.CharField(max_length=50)
    password = forms.CharField(
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput
    )



class NewLoginForm(LoginForm):
    email = forms.EmailField(validators=[checkLoginEmail])

    # through class meta we can manage the position of emailfield
    class Meta:
        model = User
        fields = ("email", "password")
        exclude = ('username',)

class LoginForm(forms.Form):

    username = forms.CharField(max_length=50)
    password = forms.CharField(
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput
    )









