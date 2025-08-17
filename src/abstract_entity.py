from abc import ABC, abstractmethod


class AbstractEntity(ABC):
    """
    Абстрактный класс для сущностей с общими свойствами.
    """

    @abstractmethod
    def __init__(self, name: str, description: str):
        """
        Инициализация абстрактной сущности.

        :param name: Название сущности
        :param description: Описание сущности
        """
        self.name = name
        self.description = description
