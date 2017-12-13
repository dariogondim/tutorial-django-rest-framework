from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from .veiculo import Veiculo

class Especial(Veiculo):
    potencia_motor = models.FloatField()
    zero_100_seg = models.FloatField()
    vel_maxima = models.FloatField()
    nv_conforto = models.FloatField()
                
    def save(self, *args, **kwargs):        
        if(self.potencia_motor > 2000 or  self.potencia_motor < 20):
            raise ValueError('A potência do motor é medida em CV e deve estar entre 20 e 2000')                    
        elif(self.zero_100_seg > 20 or self.zero_100_seg < 1):
            raise ValueError('0 a 100 é medido em segundos e deve estar entre 1 e 20')                    
        elif(self.vel_maxima > 500 or self.vel_maxima  < 20):
            raise ValueError('A velocidade máxima é medida em KM/H e deve estar entre 20 e 500')                    
        elif(self.nv_conforto > 10 or self.nv_conforto  < 0):
            raise ValueError('O nível conforto é uma nota que escala de 0 a 10')                    
        super(Especial, self).save(*args, **kwargs)

     


