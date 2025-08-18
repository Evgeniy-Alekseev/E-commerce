class CreatableMixin:
    """
    Миксин, который при создании объекта печатает информацию о классе и параметрах создания.
    """

    def __init__(self, *args, **kwargs):
        """
        Инициализация миксина.
        Печатает информацию о создании объекта.
        """
        # Вызываем __repr__ для получения строкового представления создания объекта
        print(repr(self))
        # Вызываем super().__init__ если он существует в следующем классе в MRO
        super().__init__(*args, **kwargs)  # type: ignore

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для отладки и логирования.

        :return: Строковое представление создания объекта
        """
        # Получаем имя класса
        class_name = self.__class__.__name__
        # Получаем аргументы, переданные в конструктор

        attrs = []
        if hasattr(self, 'name'):
            attrs.append(repr(self.name))
        if hasattr(self, 'description'):
            attrs.append(repr(self.description))
        if hasattr(self, 'price'):
            attrs.append(repr(self.price))
        if hasattr(self, 'quantity'):
            attrs.append(repr(self.quantity))

        # Добавляем дополнительные атрибуты для Smartphone
        if hasattr(self, 'efficiency'):
            attrs.append(repr(self.efficiency))
        if hasattr(self, 'model'):
            attrs.append(repr(self.model))
        if hasattr(self, 'memory'):
            attrs.append(repr(self.memory))
        if hasattr(self, 'color'):
            attrs.append(repr(self.color))

        # Добавляем дополнительные атрибуты для LawnGrass
        if hasattr(self, 'country'):
            attrs.append(repr(self.country))
        if hasattr(self, 'germination_period'):
            attrs.append(repr(self.germination_period))

        return f"{class_name}({', '.join(attrs)})"
