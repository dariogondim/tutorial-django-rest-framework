from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Sinistro(models.Model):
    veiculo = models.ForeignKey('veiculo', related_name='sinistro_veiculo',on_delete=models.CASCADE)
    cliente = models.ForeignKey('cliente', related_name='sinistro_cliente',on_delete=models.CASCADE)
    dt_ocorrencia  = models.DateTimeField()
    valor_pago  = models.DecimalField(max_digits=8,decimal_places=2)
    valor_coberto  = models.DecimalField(max_digits=8,decimal_places=2)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    user_cadastro = models.ForeignKey('auth.User', related_name='sinistro_us_cad',on_delete=models.CASCADE)

    class Meta:
         ordering = ('data_cadastro',)      
                
    def save(self, *args, **kwargs):                
        super(Sinistro, self).save(*args, **kwargs)

     


