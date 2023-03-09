from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(cls, file):
        raise NotImplementedError("Método não implementado")
