from django import forms
from .models import Users

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['funcao', 'cpf', 'endereco', 'telefone', 'cep', 'cargo', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Descreva sua experiência ou interesses...'}),
        }

