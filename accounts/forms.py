from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email').strip()
        password = self.cleaned_data.get('password').strip()

        if email and password:
            qs = User.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('Такого пользователя нет!')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Пароль неверный!')

            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Аккаунт отключен!')

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Введите e-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Введите пароль повторно', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email',)
    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password2']