from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class VeiculoSerializer(serializers.HyperlinkedModelSerializer):
    user_cadastro = serializers.ReadOnlyField(source='user_cadastro.username')    
    class Meta:
        model = Veiculo
        fields = ('id','tipo', 'placa', 'cor', 'modelo',
                  'ano', 'chassi', 'capacidade', 'data_cadastro', 'user_cadastro')

class  EspecialSerializer(serializers.HyperlinkedModelSerializer):
    user_cadastro = serializers.ReadOnlyField(source='user_cadastro.username')    
    class Meta:
        model = Especial
        fields = ('id','tipo', 'placa', 'cor', 'modelo',
                  'ano', 'chassi', 'capacidade', 'data_cadastro', 'user_cadastro',
                  'potencia_motor','zero_100_seg','vel_maxima','nv_conforto')

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    user_cadastro = serializers.ReadOnlyField(source='user_cadastro.username')    
    class Meta:
        model = Cliente
        fields = ('id','tipo_pessoa', 'sexo', 'nome', 'cpf_cnpj',
                  'dt_nascimento', 'data_cadastro', 'user_cadastro')               

class TabelaPrecosSerializer(serializers.HyperlinkedModelSerializer):
    user_cadastro = serializers.ReadOnlyField(source='user_cadastro.username')    
    class Meta:
        model = TabelaPrecos
        fields = ('id','veiculo', 'valor',  'data_cadastro', 'user_cadastro') 

class SinistroSerializer(serializers.HyperlinkedModelSerializer):
    user_cadastro = serializers.ReadOnlyField(source='user_cadastro.username')    
    class Meta:
        model = Sinistro
        fields = ('id','veiculo','cliente','valor_pago','valor_coberto','dt_ocorrencia','data_cadastro', 'user_cadastro') 

class AluguelSerializer(serializers.HyperlinkedModelSerializer):
    user_cadastro = serializers.ReadOnlyField(source='user_cadastro.username')    
    valor = serializers.ReadOnlyField()
    valor_seguro = serializers.ReadOnlyField()
    class Meta:
        model = Aluguel
        fields = ('id','veiculo', 'cliente',  'dt_saida', 'dt_devolucao','valor','is_segurado','valor_seguro',
        'data_cadastro','user_cadastro')                                      

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username' )