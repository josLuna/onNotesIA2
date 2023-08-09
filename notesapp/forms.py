from django import forms  
from django.forms import ModelForm
from .models import Regist,tarea  
class NewRegist(forms.ModelForm):  
    class Meta:  
        model = Regist  
        fields = "__all__"  

def clean_email(self):
     correo_electronico = self.cleaned_data('email')
     if Regist.objects.filter(email=correo_electronico).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
     return correo_electronico

class LoginForm(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=200)

class NewTarea(forms.ModelForm):  
    class Meta:  
        model = tarea  
        fields = "__all__"  