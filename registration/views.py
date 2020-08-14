from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from .forms import UserCreationFormWithEmail

# Create your views here.
class SingUpView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') +'?registrer'

    def get_form(self, form_class=None):
        form = super(SingUpView, self).get_form()
        # Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'input-line full-width', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'input-line full-width', 'placeholder':'Dirección email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'input-line full-width', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'input-line full-width', 'placeholder':'Repite la contraseña'})
        return form