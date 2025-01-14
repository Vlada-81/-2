import doctest
class DataStructure:

    def __init__(self, capacity: int, data_type: type):
        """
                Создание и подготовка к работе объекта "Структура данных"

                :param capacity : Максимальная вместимость структуры.
                :param data_type: Тип данных, хранимых в структуре.

                >>> SocialNetwork = SocialNetwork(instagram, 1300000000)
                """

        if capacity <= 0:
            raise ValueError("Вместимость структуры должна быть положительным числом.")
        self.capacity = capacity
        self.data_type = data_type

    def insert(self, item: Any) -> None:

        """
        Вставка элемента в структуру.
      param item: Элемент для вставки.  Должен соответствовать типу `data_type`.

        :return: Сообщение о вставке элемента.

          >>>  ConcreteStructure=DataStructure:
            ...    def insert(self, item: Any) -> None:
            ...        if not isinstance(item, self.data_type):
            ...            raise TypeError("Тип элемента не соответствует типу структуры")
            ...        # Реализация добавления элемента
            ...        print(f"Элемент {item} вставлен")
            >>> struct = ConcreteStructure(100, int)
            >>> struct.insert(1)
            Элемент 1 вставлен

        """
    def remove(self, item: Any) -> Optional[Any]:
        """
        Удаление элемента из структуры.

        :param item: Элемент для удаления. Должен соответствовать типу `data_type`.
        :return: Удаленный элемент, если он был найден, иначе None.
        >>> ConcreteStructure=DataStructure:
           ...   def remove(self, item: Any) -> Optional[Any]:
           ...       if not isinstance(item, self.data_type):
           ...            raise TypeError("Тип элемента не соответствует типу структуры")
           ...       return item
           >>> struct = ConcreteStructure(100, int)
           >>> struct.remove(1)
           1
        True
        """
        if __name__ == "__main__":
            doctest.testmod()