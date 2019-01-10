from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)

User = get_user_model()

class Userloginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('usernamme')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('El usuario no existe')
            if not user.check_password(password):
                raise forms.ValidationError('Password incorrecta')
            if not user.is_active:
                raise forms.ValidationError('El usuario esta desactivado')
        return super(Userloginform, self).clean(*args, **kwargs)


class Userregisterform(forms.ModelForm):
    email = forms.EmailField(label='email')
    email2 = forms.EmailField(label='Confirme email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError('Los emails no coinciden')
        emails_qs = User.objects.filter (email=email)
        if email_qs.exist():
            raise forms.ValidationError('El email ya existe')
        return(email)
