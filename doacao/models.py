from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Doacao(models.Model):
    utilizador = models.ForeignKey(User, on_delete=models.SET_NULL,null = True)
    nib = models.CharField(max_length=21, validators=[RegexValidator(r'^\d{21}$')],  default='')
    quantia =  models.DecimalField(max_digits=20, decimal_places=2)
    dataDoacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'dataDoacao'

    def __str__(self):
        return str(self.dataDoacao)
