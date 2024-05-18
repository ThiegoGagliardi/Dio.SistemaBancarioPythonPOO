from abc import ABC, abstractproperty, abstractstaticmethod

class Transacao(ABC):

    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractstaticmethod
    def registrar(self, conta):
        pass