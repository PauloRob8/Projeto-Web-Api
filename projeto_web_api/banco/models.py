from django.db import models

# Create your models here.
class Usuario(models.Models):
    gender = ('M', 'Masculino'),('F','Feminino')
    nome = models.CharField(max_length=200)
    genero = models.CharField(max_length=1,choices = gender)
    senha = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    saldo = models.FloatField()


class Conta(models.Models):
    tipo_conta = ('P','Poupança'),('C','Corrente')
    nome = models.CharField(max_length=100)
    saldo = models.FloatField()
    tipo = models.CharField(max_length=1,choices = tipo_conta)
    instituicao = models.CharField(max_length=100)
    usuario = models.ForeingKey(Usuario,on_delete = models.CASCADE)

class Cartao(models.Models):
    tipo_cartao = ('D','Débito'),('C','Crédito')
    tipo = models.CharField(max_length=1,choices=tipo_cartao)
    limite = models.FloatField()
    conta = models.ForeingKey(Conta,on_delete=models.CASCADE)
    data_encerramento_fatura = models.DateField()
    data_vencimento = models.DateField()
    bandeira = models.CharField(max_length=20)
    usuario = models.ForeingKey(Usuario,on_delete=models.CASCADE)
    numero = models.IntegerField()


class Fatura(models.Models):
    cartao = models.ForeingKey(Cartao,on_delete=moldes.CASCADE)
    referencia = models.CharField(max_length=200)
    valor = models.FloatField()

class Lançamento(models.Models):
    conta = models.ForeingKey(Conta,on_delete= models.CASCADE)
    fatura = models.ForeingKey(Fatura,on_delete=models.CASCADE)
    valor = models.FloatField()
    descricao = models.CharField(max_length=300)
    categoria = models.CharField(max_length=50)
    data = models.DateField()

