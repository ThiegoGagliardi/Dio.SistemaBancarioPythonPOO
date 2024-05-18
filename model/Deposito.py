from datetime import datetime
from model.Transacao import Transacao

class Deposito(Transacao):

    def __init__(self, valor, saldo_anterior, saldo_atual):

        self._data  = datetime.now()
        self._valor = valor
        self._saldo_anterior = saldo_anterior
        self._saldo_atual  = saldo_atual

    @property    
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        conta.extrato.adicionar_transacao(self)


    def __str__(self) :
        return f"""Deposito no valor de R$ {"{:.2f}".format(self._valor)} realizado em {self._data}, saldo alterado de R$ {"{:.2f}".format(self._saldo_anterior)} para R$ {"{:.2f}".format(self._saldo_atual)}.""";
    
