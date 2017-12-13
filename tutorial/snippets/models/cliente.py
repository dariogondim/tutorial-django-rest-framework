from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Cliente(models.Model):
    TIPO_PESSOA  =  ( 
    ( 'FIS' ,  'Física' ), 
    ( 'JUR' ,  'Jurídica' ),  
    )
    SEXO  =  ( 
    ( 'M' ,  'Masculino' ), 
    ( 'F' ,  'Feminino' ),  
    )
    tipo_pessoa = models.CharField(
        max_length=3,
        choices=TIPO_PESSOA,
        default='FIS',
    )
    sexo = models.CharField(
        max_length=1,
        choices=SEXO,
    )
    nome =  models.CharField(max_length=70)    
    cpf_cnpj =  models.CharField(max_length=14)    
    dt_nascimento = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    user_cadastro = models.ForeignKey('auth.User', related_name='cliente_us_cad',on_delete=models.CASCADE)

    class Meta:
         ordering = ('data_cadastro',)      
                
    def save(self, *args, **kwargs):                
        super(Cliente, self).save(*args, **kwargs)

     


