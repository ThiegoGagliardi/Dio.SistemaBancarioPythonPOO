from model.Conta import Conta

class Cliente:
    def __init__(self,endereco):
        self._endereco         = endereco
        self._contas           = []

    def adicionar_conta(self,conta):
        self._contas.append(conta)

    def buscar_conta(self, numero):
        
        for conta in self._contas:
            if (str(conta.numero) == numero):
                return conta
        
        return None

    def listar_contas(self):

        msg = '';
    
        for conta in self._contas:
            msg += f'''{conta} '''

        return msg