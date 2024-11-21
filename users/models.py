from django.db import models
from django.contrib.auth.models import User
from cpf_field.models import CPFField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
import uuid


class Users(User):
    userid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CHOICES = [
        ('P', 'Prestador'),
        ('C', 'Cliente')
    ]
    funcao = models.CharField(max_length=100,choices=CHOICES, null=False, blank=False)
    cpf = CPFField('cpf')
    endereco = models.CharField(max_length=150, null=False, blank=False)
    telefone = PhoneNumberField(blank=True)
    cep = models.CharField(
        max_length=9,
        validators=[
            RegexValidator(
                regex=r'^\d{5}-\d{3}$',
                message='O CEP deve estar no formato 12345-678.',
            )
        ],
    )
    cargo = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

