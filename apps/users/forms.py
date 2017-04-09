from django import forms
from django.contrib import auth

from apps.users.models import AuthUser


class LoginForm(forms.Form):
    attrs = {
        'class': 'form-control',
    }
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名'}))
    password = forms.CharField(max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码'}))

    def __init__(self, *args, **kwargs):
        self.user = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        self.user = auth.authenticate(username=username, password=password)

        if self.user:
            if not self.user.is_active:
                raise forms.ValidationError('用户未激活')
        else:
            raise forms.ValidationError('用户名或密码错误')


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=20,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名'}))
    password = forms.CharField(min_length=4, max_length=20,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}))
    password2 = forms.CharField(min_length=4, max_length=20,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请再次输入密码'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if AuthUser.objects.filter(username=username).count() > 0:
            raise forms.ValidationError('用户名已存在')
        return username

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError('两次密码不一致')
        return password2
