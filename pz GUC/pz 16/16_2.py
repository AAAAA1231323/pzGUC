#2    вариант 5

#Создайте класс "Фрукт", который содержит информацию о наименовании и весе
#фрукта. Создайте классы "Яблоко" и "Апельсин", которые наследуются от класса
#"Фрукт" и содержат информацию о цвете.





class Fruit:

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight


class Apple(Fruit):

    def __init__(self, name: str, weight: float, color: str):
        super().__init__(name, weight)
        self.color = color


class Orange(Fruit):

    def __init__(self, name: str, weight: float, color: str):
        super().__init__(name, weight)
        self.color = color


if __name__ == "__main__":
    apple = Apple("Яблоко", 0.15, "Красный")
    print(f"Фрукт: {apple.name}")
    print(f"Вес: {apple.weight} кг, Цвет: {apple.color}")
    print("-" * 30)

    orange = Orange("Апельсин", 0.25, "Оранжевый")
    print(f"Фрукт: {orange.name}")
    print(f"Вес: {orange.weight} кг, Цвет: {orange.color}")
