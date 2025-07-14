from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.Form):
    nome = forms.CharField(
        label='Nome completo',
        widget=forms.TextInput(attrs={'placeholder': 'Seu nome completo'})
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'placeholder': 'seuemail@exemplo.com'})
    )
    mensagem = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(attrs={
            'placeholder': 'Digite sua mensagem aqui',
            'rows': 4,
            'style': 'height: 150px'
        })
    )
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
