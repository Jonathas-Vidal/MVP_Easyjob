from django import forms
from .models import Users

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}),
        min_length=8,  # Você pode ajustar o mínimo de caracteres conforme necessário
        required=True
    )

    class Meta:
        model = Users
        fields = ['username', 'password', 'funcao', 'cpf', 'endereco', 'telefone', 'cep', 'cargo', 'descricao']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o seu nome'}),
            'descricao': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Descreva sua experiência ou interesses...', 'class': 'form-control'}),
            'funcao': forms.Select(attrs={'class': 'form-select'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12345-678'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: (99) 99999-9999'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 123.456.789-00'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu endereço'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o cargo ou profissão'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Aplica o hash na senha
        if commit:
            user.save()
        return user