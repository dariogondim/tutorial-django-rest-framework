# Generated by Django 2.0 on 2017-12-12 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_auto_20171212_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='cor',
            field=models.CharField(choices=[('AZUL', 'Azul'), ('VERMELHO', 'Vermelho'), ('VERDE', 'Verde'), ('AMARELO', 'Amarelo'), ('BRANCO', 'Branco'), ('PRETO', 'Preto'), ('PRATA', 'Prata')], default='PRETO', max_length=8),
        ),
    ]