from model.Extrato import Extrato
from model.Deposito import Deposito
from model.Saque import Saque

from datetime import datetime

class Conta:

    AGENCIA = '0001'
    sequencia_numero_conta = 0

    def __init__(self,numero, cliente):       

        self._numero        = numero
        self._agencia       = self.AGENCIA;
        self._saldo         = 0
        self._cliente       = cliente;
        self._extrato       = Extrato();

    def __str__(self):
       return f'{self._agencia} - {self._numero}'
    
    @classmethod
    def criar_nova_conta(cls, cliente):                
        cls.sequencia_numero_conta += 1;

        return cls(cls.sequencia_numero_conta, cliente)

    @property
    def agencia(self):
      return self._agencia;
    
    @property
    def numero(self):
      return self._numero;
    
    @property    
    def saldo(self):
        return self._saldo;

    @property    
    def extrato(self):
        return self._extrato;

    def depositar(self,valor_deposito):
   
       if valor_deposito > 0: 
         
            saldo_atual = self._saldo;
     
            self._saldo =+ valor_deposito
     
            Deposito(valor_deposito,saldo_atual,self._saldo).registrar(self)

            return [True,"Deposito realizado com sucesso"]     
       else:  
            return [False,"Deposito não realizado, valor inválido"]


    def sacar(self,valor_saque):   
   
       pode_sacar, mensagem = self.pode_realizar_saque(valor_saque)

       if (pode_sacar):

         saldo_atual = self._saldo;        
               
         self._saldo -= valor_saque

         Saque(valor_saque,saldo_atual,self._saldo).registrar(self)
      
         return [True, mensagem]
       else:
          return [False,mensagem]
   
    def pode_realizar_saque(self,valor_saque):

        if (self.verificar_saldo_maior_valor_saque(valor_saque)):      
            return [False, "Saldo insuficiente"]
   
        return [True,""]

    def verificar_saldo_maior_valor_saque(self,valor_saque):
        return valor_saque > self._saldo

    def verificar_extrato(self):
        return self._extrato.montar_extrato()
   
   