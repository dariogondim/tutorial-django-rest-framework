from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class TabelaPrecos(models.Model):
    veiculo = models.ForeignKey('veiculo', related_name='tabela_precos_veiculo',on_delete=models.CASCADE)
    valor  = models.DecimalField(max_digits=5,decimal_places=2)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    user_cadastro = models.ForeignKey('auth.User', related_name='tabela_precos_us_cad',on_delete=models.CASCADE)

    class Meta:
         ordering = ('data_cadastro',)      
                
    def save(self, *args, **kwargs):                
        super(TabelaPrecos, self).save(*args, **kwargs)

     


