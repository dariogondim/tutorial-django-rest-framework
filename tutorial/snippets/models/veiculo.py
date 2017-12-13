from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Veiculo(models.Model):
    TIPO  =  ( 
    ( 'COMB' ,  'Combustão' ), 
    ( 'ELET' ,  'Elétrico' ),  
    )
    COR  =  ( 
    ( 'AZUL' ,  'Azul' ), 
    ( 'VERMELHO' ,  'Vermelho' ),  
    ( 'VERDE' ,  'Verde' ),  
    ( 'AMARELO' ,  'Amarelo' ),  
    ( 'BRANCO' ,  'Branco' ),
    ( 'PRETO' ,  'Preto' ),
    ( 'PRATA' ,  'Prata' ),
    )
    tipo = models.CharField(
        max_length=4,
        choices=TIPO,
        default='COMB',
    )
    cor = models.CharField(
        max_length=8,
        choices=COR,
        default='PRETO',
    )
    placa =  models.CharField(max_length=10)    
    modelo =  models.TextField()
    ano =  models.PositiveSmallIntegerField()
    chassi =  models.CharField(max_length=25)
    capacidade =  models.PositiveSmallIntegerField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    user_cadastro = models.ForeignKey('auth.User', related_name='veiculo_us_cad',on_delete=models.CASCADE)

    class Meta:
         ordering = ('data_cadastro',)      
                
    def save(self, *args, **kwargs):
        if(self.ano < 2000 or self.ano > 2018):
            raise ValueError('O ano está fora de faixa 2000 - 2018')           
        elif(self.capacidade > 2 or self.capacidade < 100):
            raise ValueError('a capacidade de pessoas deve estar entre 2 e 100') 
        super(Veiculo, self).save(*args, **kwargs)

     


