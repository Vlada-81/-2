import doctest
class SocialNetwork:

    def init(self, name: str, users: float):
        """
                Создание и подготовка к работе объекта "Социальная сеть"

                :param name: Название социальной сети.
                :param users: Количество пользователей.

                >>> SocialNetwork = SocialNetwork(instagram, 1300000000)
                """
        if not isinstance(name, (str)):
            raise TypeError("Название социальной сети должен быть типа str")
        if users <= 0:

            raise ValueError("Количество подписчиков должено быть положительным числом.")

        self.name = name

        self.users = users

    def add_user(self, user_id: int, user_info: Dict[str, Any]) -> None:

        """
        Добавление пользователя в социальную сеть.
        param user_id: Идентификатор пользователя.
        param user_info: Словарь с информацией о пользователе.

        :return: Сообщение о добавлении пользователя.

         >>> ConcreteNetwork=SocialNetwork:
            ...    def add_user(self, user_id: int, user_info: Dict[str, Any]) -> None:
            ...        print(f"Пользователь {user_id} добавлен")
            >>> net = ConcreteNetwork("instagram", 1300000000)
            >>> net.add_user(1, {"name": "Test"})
            Пользователь 1 добавлен

        """
        ...
    def get_user_info(self, user_id: int) -> Optional[Dict[str, Any]]:
        """
        Метод получения информации о пользователе.

        :param user_id: Идентификатор пользователя.
        :return: Словарь с информацией о пользователе, если пользователь найден, иначе None.
         >>> ConcreteNetwork=SocialNetwork:
            ...    def get_user_info(self, user_id: int) -> Optional[Dict[str, Any]]:
            ...        return {"name":"Test", "age": 22}
            >>> net = ConcreteNetwork("instagram", 1300000000)
            >>> net.get_user_info(1)
            {'name': 'Test', 'age': 22}
        True
        """
        if __name__ == "__main__":
            doctest.testmod()