from model.Cliente import Cliente

class PessoaFisica(Cliente):

    def __init__(self,cpf, nome, data_nascimento, endereco):
        
        super().__init__(endereco)

        self._cpf = cpf
        self._nome             = nome
        self._data_nascimento  = data_nascimento

    def __str__(self):
        return f'{self._nome} - {self._cpf} {self._endereco}' 
        
    @property
    def cpf(self):
        return self._cpf;


