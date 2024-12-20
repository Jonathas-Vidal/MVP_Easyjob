# Generated by Django 5.1.3 on 2024-11-21 02:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidacy',
            fields=[
                ('idCandidatura', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dataCandidatura', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('idServico', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('setor', models.CharField(choices=[('SA', 'Saúde'), ('TI', 'Tecnologia da Informação'), ('ED', 'Educação'), ('FI', 'Finanças'), ('CO', 'Comércio'), ('IN', 'Indústria'), ('AG', 'Agronegócio'), ('TR', 'Transportes'), ('AR', 'Artes e Design'), ('CC', 'Construção Civil'), ('EN', 'Engenharia'), ('JU', 'Jurídico'), ('MA', 'Marketing e Publicidade'), ('ME', 'Mídia e Entretenimento'), ('RH', 'Recursos Humanos'), ('AL', 'Alimentação'), ('HO', 'Hotelaria e Turismo'), ('SE', 'Segurança'), ('EN', 'Energia e Meio Ambiente'), ('CS', 'Ciências e Pesquisa'), ('ES', 'Esportes e Lazer'), ('IM', 'Imobiliário'), ('AD', 'Administração'), ('LO', 'Logística e Suprimentos'), ('CM', 'Comunicação e Jornalismo'), ('PE', 'Petróleo e Gás'), ('BI', 'Biotecnologia e Farmacêutica'), ('GA', 'Governo e Políticas Públicas'), ('CU', 'Cultura e Patrimônio'), ('RE', 'Religião e Assistência Social'), ('SG', 'Serviços Gerais'), ('EL', 'Elétrica'), ('SD', 'Saúde e Bem-Estar'), ('LM', 'Limpeza e Conservação'), ('JM', 'Jardinagem e Manutenção Externa'), ('BR', 'Beleza e Estética'), ('ME', 'Mecânica e Reparos Automotivos'), ('PS', 'Pessoal e Assistência'), ('SE', 'Segurança e Vigilância')], max_length=100)),
            ],
        ),
    ]
