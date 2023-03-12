"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""

class Worker():

    def __init__(self, name, surname, position, wage, bonus):
        self.incomes = {"wage": wage, "bonus": bonus}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = self.incomes["wage"]
        self.bonus = self.incomes["bonus"]

    def __str__(self):
        result = self.incomes["wage"] + self.incomes["bonus"]
        return f"{self.name} {self.surname} работает как {self.position} и вместе с премией получает {result}"


class Position():
    def __init__(self, worker):
        self.incomes = {"wage": worker._income, "bonus": worker.bonus}
        self.name = worker.name
        self.surname = worker.surname
        self.position = worker.position
        self._income = worker.incomes["wage"]

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        total_income = self.incomes["wage"] + self.incomes["bonus"]
        print(f"Полный доход составляет {total_income}")


worker = Worker("Василий", "Синицын", "Гереральный деректор", 100000, 50000)
worker_pos = Position(worker)
worker_pos.get_full_name()
worker_pos.get_total_income()

print(worker)