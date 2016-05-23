from django import forms

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

class ChatForm(forms.Form):
	escriu = forms.CharField(max_length=100,required=True)


	