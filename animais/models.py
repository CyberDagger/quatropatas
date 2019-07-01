from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Animal(models.Model):
    ESPECIE_OPCOES = (('Cão', 'Cão'), ('Gato', 'Gato'))
    GENERO_OPCOES = (('Macho', 'Macho'), ('Fêmea', 'Fêmea'))

    nome = models.CharField(max_length=200)
    slug = models.SlugField()
    especie = models.CharField(max_length=10, choices=ESPECIE_OPCOES, default='Cão')
    raca = models.CharField(max_length=200)
    genero = models.CharField(max_length=10, choices=GENERO_OPCOES, default='M')
    idade = models.PositiveSmallIntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(default='default.png')

    def __str__(self):
        return self.nome

class Comentario(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(auto_now_add=True)
    texto = models.TextField()

    ordering = ['-data']

    def __str__(self):
        return str(self.data)

class Adocao(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    telefone = models.IntegerField()
    #telefone = PhoneNumberField()
    data = models.DateField()
    hora = models.TimeField(default="00:00")
    concretizada = models.BooleanField(default=False)

    def __str__(self):
        return str(self.animal)
