class Extrato:

    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)

    @property
    def transacoes(self):
      return self._transacoes 

    def montar_extrato(self):
        
        extrato = ''

        for trasancao in  self._transacoes:
            extrato += f'''{trasancao}''' 

        return extrato