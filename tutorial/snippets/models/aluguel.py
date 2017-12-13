from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from .tabela_precos import TabelaPrecos
from .veiculo import Veiculo
from .especial import Especial

from decimal import Decimal
import datetime

class Aluguel(models.Model):
    
    veiculo = models.ForeignKey('veiculo', related_name='aluguel_veiculo',on_delete=models.CASCADE)
    cliente = models.ForeignKey('cliente', related_name='aluguel_cliente',on_delete=models.CASCADE)
    dt_saida  = models.DateTimeField()
    dt_devolucao  = models.DateTimeField()
    valor  = models.DecimalField(max_digits=8,decimal_places=2)
    is_segurado = models.BooleanField()
    valor_seguro = models.DecimalField(max_digits=8,decimal_places=2)   
    data_cadastro = models.DateTimeField(auto_now_add=True)
    user_cadastro = models.ForeignKey('auth.User', related_name='aluguel_us_cad',on_delete=models.CASCADE)

    class Meta:
         ordering = ('data_cadastro',)      

    def set_preco_alugel(self, *args, **kwargs):     
        if(self.dt_devolucao < self.dt_saida):
            raise ValueError('A data de devolução deve ser maior que a data de saida') 
        #obtém o último valor cadastrado na tabela de preços daquele veículo
        queryset = TabelaPrecos.objects.filter(veiculo = self.veiculo).last()
        if(queryset == None):
             raise ValueError('Não há valores registrados na tabela de preços para esse veículo') 
        periodo = self.dt_devolucao - self.dt_saida;
        qtdDias  = periodo.days            
        #ultrapassar 2 horas ja conta mais um dia sendo no mínimo 1 dia independente da quantidade de dias
        if((periodo.total_seconds()  - periodo.days*86400 > 7200) or qtdDias == 0):
            qtdDias+=1
        """    
            verifica se o valor informado do aluguel condiz com a política de desconto e preços da empresa:            
                aluguel ate 1 dia preço/dia = 100%
                aluguel entre 3 e 5 dias desconto 10%
                aluguel entre 6 e 10  dias desconto 20%
                aluguel acima de 10 dias desconto 25%
                seguro ate 5 dias  + 20% valor
                seguro ate 10 dias  + 30% valor
                seguro a partir 10 dias  + 40% valor
        """
        #print("qtd Dias",qtdDias)
        valor = qtdDias * queryset.valor
        if(qtdDias >= 3 and qtdDias <= 5):
            valor = Decimal(0.9)*valor            
        elif(qtdDias >= 6 and qtdDias <= 10):
            valor = Decimal(0.8)*valor
        elif(qtdDias > 10):    
            valor =Decimal(0.7)*valor
        #print("valor aplicado desconto",valor)
        if(self.is_segurado):
            if(qtdDias < 5):    
                valor_seguro = Decimal(1.2)*valor - valor
            elif(qtdDias >= 5 and qtdDias <= 10):
                valor_seguro =Decimal(1.3)*valor - valor
            elif(qtdDias > 10):
                valor_seguro = Decimal(1.4)*valor - valor
        else:
            if(Especial.objects.filter(veiculo_ptr = self.veiculo).exists()):
                raise ValueError("O seguro é obrigatório se tratando de Veículos Especiais ")
            valor_seguro = Decimal(0.0)        
        #print("valor seguro",valor_seguro)            
        valor = round(valor,2);    
        valor_seguro = round(valor_seguro,2)
        self.valor = valor
        self.valor_seguro = valor_seguro
        #print("valor final",valor + valor_seguro)        
        
    def save(self, *args, **kwargs):
        self.set_preco_alugel(self, *args, **kwargs)                
        super(Aluguel, self).save(*args, **kwargs)




