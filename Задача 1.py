
class table:

    def init(self, material: str, weight: float):
        """
                Создание и подготовка к работе объекта "Стол"

                :param material: Материал стола.
                :param weight: Вес стола.
                >>> table = table(wood, 20)
                """
        if not isinstance(material, (str)):
            raise TypeError("Материал изделия должен быть типа str")
        if weight <= 0:

            raise ValueError("Вес должен быть положительным числом.")

        self.material = material

        self.weight = weight

    def assemble(self) -> None:

        """

        Собрать стол.

        :return: Сообщение о завершении сборки.

        >>> table = table("wood", 15)

        >>> table.assemble()

        'Стол собран.'

        """
        ...
    def move(self, new_location: str) -> bool:
        """
        Переместить стол в новое место.

        :param new_location: Новое местоположение.
        :return: Успешно ли перемещение.
        >>> table = table("wood", 10)
        >>> table.move("living room")
        True
        """
       
