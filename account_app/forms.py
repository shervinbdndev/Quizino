from django import forms
from django.core import validators






class LoginForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'نام کاربری خود را وارد کنید',
            },
        )
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'کد ملی خود را وارد کنید'
            },
        ),
        validators=[
            validators.MinLengthValidator(limit_value=10),
            validators.MaxLengthValidator(limit_value=10),
        ],
    )








class RegisterForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'نام خود را وارد کنید',
            }
        )
    )
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'نام خانوادگی خود را وارد کنید',
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل خود را وارد کنید',
            }
        )
    ,
    validators=[
        validators.EmailValidator()
        ],
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'کدملی خود را وارد کنید',
            }
        ),
        validators=[
            validators.MinLengthValidator(limit_value=10),
            validators.MaxLengthValidator(limit_value=10),
        ],
    )
    
    conf_pass = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'کدملی خود را دوباره وارد کنید',
            }
        ),
        validators=[
            validators.MinLengthValidator(limit_value=10),
            validators.MaxLengthValidator(limit_value=10),
        ],
    )
