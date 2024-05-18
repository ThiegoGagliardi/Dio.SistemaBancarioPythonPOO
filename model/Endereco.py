class Endereco:

    def __init__(self,logradouro, numero,bairro, cidade, uf):
        self._logradouro = logradouro
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade
        self._uf     = uf
    

    def __str__(self) -> str:
        return f'{self._logradouro}, numero:{self._numero}, bairro:{self._bairro}, cidade{self._cidade} - {self._uf}'