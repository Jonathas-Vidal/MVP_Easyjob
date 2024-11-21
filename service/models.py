from django.db import models
import uuid
from users.models import Users

class Service(models.Model):
    SETOR_CHOICES = [
    ('SA', 'Saúde'),
    ('TI', 'Tecnologia da Informação'),
    ('ED', 'Educação'),
    ('FI', 'Finanças'),
    ('CO', 'Comércio'),
    ('IN', 'Indústria'),
    ('AG', 'Agronegócio'),
    ('TR', 'Transportes'),
    ('AR', 'Artes e Design'),
    ('CC', 'Construção Civil'),
    ('EN', 'Engenharia'),
    ('JU', 'Jurídico'),
    ('MA', 'Marketing e Publicidade'),
    ('ME', 'Mídia e Entretenimento'),
    ('RH', 'Recursos Humanos'),
    ('AL', 'Alimentação'),
    ('HO', 'Hotelaria e Turismo'),
    ('SE', 'Segurança'),
    ('EN', 'Energia e Meio Ambiente'),
    ('CS', 'Ciências e Pesquisa'),
    ('ES', 'Esportes e Lazer'),
    ('IM', 'Imobiliário'),
    ('AD', 'Administração'),
    ('LO', 'Logística e Suprimentos'),
    ('CM', 'Comunicação e Jornalismo'),
    ('PE', 'Petróleo e Gás'),
    ('BI', 'Biotecnologia e Farmacêutica'),
    ('GA', 'Governo e Políticas Públicas'),
    ('CU', 'Cultura e Patrimônio'),
    ('RE', 'Religião e Assistência Social'),
    ('SG', 'Serviços Gerais'),
    ('EL', 'Elétrica'),
    ('SD', 'Saúde e Bem-Estar'),
    ('LM', 'Limpeza e Conservação'),
    ('JM', 'Jardinagem e Manutenção Externa'),
    ('BR', 'Beleza e Estética'),
    ('ME', 'Mecânica e Reparos Automotivos'),
    ('PS', 'Pessoal e Assistência'),
    ('SE', 'Segurança e Vigilância')
]
    idServico = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idPrestador = models.ForeignKey(Users, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    setor = models.CharField(max_length=100,choices=SETOR_CHOICES, null=False, blank=False)

class Candidacy(models.Model):
    idCandidatura = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idCliente = models.ForeignKey(Users,on_delete=models.CASCADE)
    idServico = models.ForeignKey(Service,on_delete=models.CASCADE)
    dataCandidatura = models.DateTimeField(auto_now_add=True, blank=False, null=False)
