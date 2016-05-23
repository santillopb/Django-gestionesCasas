from django import forms
#from django import ModelForm
from .models import Factura, NotaCalendario

"""class ContactoForm(forms.Form):
		correo = forms.EmailField(label='Tu correo electronico')
		mensaje = forms.CharField(widget=forms.TextArea)

"""
"""class Accede(ModelForm):
	class Meta:
		Model = Login
		usuario = forms.CharField(label='Usuario: ',max_length=100, required=True)
		contrassenya = forms.CharField(max_length=100, required=True)"""
"""class LoginForm(forms.LoginForm):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())"""

class ChatForm(forms.Form):
	escriu = forms.CharField(max_length=100,required=True)

class FacturaForm(forms.ModelForm):

    class Meta:
        model = Factura
        fields = ['persona', 'image', 'preu']

class AnadeNotaForm(forms.ModelForm):
	class Meta:
		model = NotaCalendario
		fields = ['nota', 'persona']