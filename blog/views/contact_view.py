from django.views.generic.edit import FormView
from blog.forms.contact_form import ContactForm
from django.core.mail import send_mail
from django.conf import settings


class ContactView(FormView):
    template_name = 'pages/contato.html'
    form_class = ContactForm
    success_url = '/contato/'

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        mensagem = form.cleaned_data['mensagem']

        corpo = f"""\
Mensagem recebida via formulário de contato:

Nome: {nome}
E-mail: {email}
Mensagem:
{mensagem}
"""

        send_mail(
            subject=f"[Contato] Mensagem de {nome}",
            message=corpo,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False
        )

        return super().form_valid(form)

    def get_success_url(self):
        return f"{self.success_url}?sucesso=1"
