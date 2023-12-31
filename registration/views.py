from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile

# Create your views here.
class SignUpViews(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


    def get_success_url(self):
        return reverse_lazy ('login') + '?register'
    
    def get_form(self, form_class = None):
        form = super(SignUpViews, self).get_form()
        #modificar el form 
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb2', 'placeholder':  'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb2', 'placeholder':  'Ingrese su email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb2', 'placeholder':  'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb2', 'placeholder':  'Ingrese su contraseña nuevamente'})
        return form 
    

@method_decorator(login_required, name= 'dispatch')
class ProfileUpdateView(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        #recuperar el objeto que se va a editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


@method_decorator(login_required, name= 'dispatch')
class EmailUpdateView(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        #recuperar el objeto que se va a editar
        return self.request.user
    
    def get_form(self, form_class=None):
        form = super(EmailUpdateView, self).get_form()
        #modificar el form 
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb2', 'placeholder':  'Ingrese su email nuevo'})
        return form   