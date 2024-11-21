from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['titulo', 'descricao', 'setor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['titulo'].widget.attrs['placeholder'] = 'Digite o título do serviço'
        self.fields['descricao'].widget.attrs['placeholder'] = 'Descreva o serviço oferecido'

