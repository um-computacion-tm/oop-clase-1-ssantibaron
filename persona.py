class Persona:
    def __init__(self,nombre:str="Santiago",apellido:str="Baron",dni:int=12345):
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__dni__ = dni

    def __str__(self):
        return f'Mis datos son nombre = {self.__nombre__} apellido = {self.__apellido__} documento = {self.__dni__}'