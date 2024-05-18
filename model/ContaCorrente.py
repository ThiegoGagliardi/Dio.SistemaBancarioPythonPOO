from model.Conta import Conta
from model.Saque import Saque

class ContaCorrente(Conta) :

    LIMITE_SAQUES_DIARIOS = 3
    LIMITE_VALOR_SAQUE    = 500

    def __init__(self, numero, cliente):

        super().__init__(numero, cliente)         
        
    def sacar(self,valor_saque):

        retorno, mensagem = super(ContaCorrente,self).sacar(valor_saque)

        return [retorno, mensagem]

    def pode_realizar_saque(self,valor_saque):
   
        if (self.verificar_excedeu_numero_saque()):      
            return [False, "Excedido o limite de saque."]
   
        if (self.verificar_excedeu_valor_saque(valor_saque)):
            return [False, "Valor maior que o permitido."]   
   
        return super(ContaCorrente,self).pode_realizar_saque(valor_saque)

    def verificar_excedeu_numero_saque(self):
        return self.verificar_numero_saques() >= self.LIMITE_SAQUES_DIARIOS

    def verificar_excedeu_valor_saque(self,valor_saque):
        return valor_saque > self.LIMITE_VALOR_SAQUE

    def verificar_numero_saques(self):
        return len([transacao for transacao in self._extrato.transacoes if type(transacao) == Saque])   