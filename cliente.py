class Cliente:

    def __init__(self, nome) -> None:
        self.__nome = nome

    @property
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        priint("chamado setter nome()")
        self.__nome = nome
