class ZeroQuantityError(Exception):
    """
    Исключение, возникающее при попытке добавить товар с нулевым количеством.
    """

    def __init__(self, message: str = "Товар с нулевым количеством не может быть добавлен"):
        """
        Инициализация исключения.

        :param message: Сообщение об ошибке
        """
        self.message = message
        super().__init__(self.message)
