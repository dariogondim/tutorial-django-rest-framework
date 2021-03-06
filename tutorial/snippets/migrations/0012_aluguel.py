# Generated by Django 2.0 on 2017-12-13 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0011_tabelaprecos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_saida', models.DateTimeField()),
                ('dt_devolucao', models.DateTimeField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('is_segurado', models.BooleanField()),
                ('valor_seguro', models.DecimalField(decimal_places=2, max_digits=7)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aluguel_cliente', to='snippets.Cliente')),
                ('user_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aluguel_us_cad', to=settings.AUTH_USER_MODEL)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aluguel_veiculo', to='snippets.Veiculo')),
            ],
            options={
                'ordering': ('data_cadastro',),
            },
        ),
    ]
